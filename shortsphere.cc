#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <vector>
uint64_t masks[1280][2] = {0};
int main(int argc, char *argv[])
{
	int max_depth = 128;
	bool solutions = false;
	bool multimode = false;
	bool onemode = false;
	bool printcount = false;
	int max_popcount = 128;
	const char *preset = "";
	for (int i = 1; i < argc; i++) {
		switch (argv[i][0]) {
			case 'u': // upper bound
				max_depth = strtol(argv[i]+1, NULL, 10);
				if (max_depth > 128)
					max_depth = 128;
				break;
			case 's': // print solutions
				solutions = true;
				break;
			case 'x': // find one solution and exit
				onemode = true;
				break;
			case 'm': // multi mode
				multimode = true;
				break;
			case 'c': // show popcount
				max_popcount = 0;
			case 'p': { // preset
				preset = argv[i]+1;
				break;
			}
		}
	}
	{
		uint8_t s[4] = {0, 1, 2, 3};
		for (int i = 0; i < 1280; i++) {
			masks[i][s[0]>>6] |= (uint64_t)1<<(s[0]&63);
			masks[i][s[1]>>6] |= (uint64_t)1<<(s[1]&63);
			masks[i][s[2]>>6] |= (uint64_t)1<<(s[2]&63);
			masks[i][s[3]>>6] |= (uint64_t)1<<(s[3]&63);
			s[0] = (s[0]+1) % 128;
			s[1] = (s[1]+3) % 127;
			s[2] = (s[2]+5) % 126;
			s[3] = (s[3]+7) % 125;
		}
	}
	struct state {
		int level;
		int depth;
		uint64_t mask[2];
		int count() {
			return __builtin_popcountl(mask[0]) + __builtin_popcountl(mask[1]);
		}
	} st;
	std::vector<state> stack;
	st.level = 0;
	st.depth = 1;
	st.mask[0] = masks[0][0];
	st.mask[1] = masks[0][1];
	{
		const char *p = preset;
		while (*p) {
			st.level += *p++ != '0' ? 10 : 1;
			st.depth += 1;
			st.mask[0] |= masks[st.level][0];
			st.mask[1] |= masks[st.level][1];
		}
	}
	int popcount = st.count();
	for (;;) {
		if (popcount > max_popcount) {
			max_popcount = popcount;
			printf("pop : %d\n", popcount);
		}
		if (st.mask[0] == ~(uint64_t)0 && st.mask[1] == ~(uint64_t)0 || st.depth >= max_depth || popcount+(max_depth-st.depth)*4 < 128) {
			if (popcount == 128) {
				if (!multimode)
					max_depth = st.depth-1;
				if (solutions) {
					char rs[129];
					memset(rs, '1', st.depth-1);
					rs[st.depth-1] = 0;
					memcpy(rs, preset, strlen(preset));
					for (auto it = stack.rbegin(); it != stack.rend(); ++it) {
						rs[it->depth-1] = '0';
					}
					printf("%d %s\n", st.depth, rs);
				} else {
					printf("%d\n", st.depth);
				}
				if (onemode)
					break;
			}
			if (stack.size() == 0)
				break;
			st = stack.back();
			stack.pop_back();
			st.level += 10;
		} else {
			stack.push_back(st);
			st.level += 1;
		}
		st.depth += 1;
		st.mask[0] |= masks[st.level][0];
		st.mask[1] |= masks[st.level][1];
		popcount = st.count();
	}
}
