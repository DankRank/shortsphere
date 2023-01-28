#!/usr/bin/env python3
import os
import traceback
import signal
# 54 00000100100011110110001001101110001010001110100100000
upperbound = 54
freejobs = {x for x in range(65536)}
freecpus = {0, 2, 4, 6, 8, 10}
children = {}
for ent in os.scandir('out'):
    if ent.name.endswith('.txt'):
        try:
            freejobs.remove(int(ent.name[:-4]))
        except ValueError:
            pass
with open('empty.txt') as f:
    for line in f:
        try:
            freejobs.remove(int(line.rstrip()))
        except ValueError:
            pass
def waitall():
    yield os.waitpid(-1, 0)
    while True:
        res = os.waitpid(-1, os.WNOHANG)
        if res == (0, 0):
            break
        yield res
try:
    while len(freejobs) or len(children):
        while len(freecpus) and len(freejobs):
            job = freejobs.pop()
            cpu = freecpus.pop()
            print(f'queueing {job} ({len(freejobs)} jobs left)')
            child = os.fork()
            if child == 0:
                try:
                    os.dup2(os.open(f'out/{job:05d}.txt', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o666), 1)
                    os.sched_setaffinity(0, [cpu])
                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                    os.execl('./shortsphere', 'shortsphere', f'u{upperbound}', 's', 'm', f'p{job:016b}')
                except:
                    traceback.print_exc()
                    os._exit(1)
            else:
                children[child] = (job, cpu)
        for pid, status in waitall():
            job, cpu = children[pid]
            del children[pid]
            freecpus.add(cpu)
            if status:
                freejobs.add(job)
                print(f'uh oh {job} failed {pid} {cpu} {status}')
                os.unlink(f'out/{job:05d}.txt')
            else:
                print(f'finished {job}')
except:
    traceback.print_exc()
    print('Waiting for things to stop...')
    try:
        while len(children):
            pid, status = os.waitpid(-1, 0)
            job, cpu = children[pid]
            del children[pid]
            if status:
                print(f'uh oh {job} failed {pid} {cpu} {status}')
                os.unlink(f'out/{job:05d}.txt')
            else:
                print(f'finished {job}')
    except:
        traceback.print_exc()
        print('Killing stuff...')
        for pid in children:
            job, cpu = children[pid]
            os.kill(pid, signal.SIGKILL)
            print(f'uh oh {job} failed {pid} {cpu} {status}')
            os.unlink(f'out/{job:05d}.txt')
