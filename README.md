# Blue Sphere shortest path

In [Blue Sphere](https://info.sonicretro.org/Blue_Sphere) each level procedurally generated by combining four chunks, which are picked out of a set of [128 predefined patterns](https://info.sonicretro.org/Blue_Sphere/Maps). If you collect all rings in a level, instead of going to the next level, you advance 10 levels. What is the smallest number of levels you have to beat (starting from level 1, without using codes) to see all 128 patterns?

The answer is 49, and there are 6 ways to do it:
```
49 100110010101010001001100101110110101010010010011
49 100110010101010010001100101110110101010010010011
49 101010010101010001001100101110110101010100010110
49 101010010101010010001100101110110101010100010110
49 101100010101010001001100101110110101010100010110
49 101100010101010010001100101110110101010100010110
```

Where 0 means complete the level normally, and 1 means complete it with all the rings. Note that there are 48 1's and 0's in the lines above, as the way you complete the 49th level doesn't matter.

## Graph
You can follow any path as long as you don't combine red and blue edges. Circled arrows mean collect all rings.

![the graph](graph.png)

## Maps
Relevant maps can be found here:
* [Route 1](mapgen/route1.md)
* [Route 2](mapgen/route2.md)
* [Route 3](mapgen/route3.md)
* [Route 4](mapgen/route4.md)
* [Route 5](mapgen/route5.md)
* [Route 6](mapgen/route6.md)

## Progression
* Jan 24:
  * Got this idea thanks to [this video](https://www.youtube.com/watch?v=L4nUrb5BoC8), the [disasm](https://github.com/sonicretro/skdisasm/), and the [map generator](https://bsgen-new.neocities.org/).
  * Initial lower bound is 32, and upper bound is 128.
* Jan 25:
  * Made a little script in Python and found a 74 level solution.
  * None of the 44-level paths visit more than 123 patterns, which rules out any solutions shorter than 46.
  * I rewrote the code in [C++](shortsphere.cc) and improved the upper bound to 72, 65, 64.
  * By manually picking various initial paths I improved the upper bound to 63, 61, 60, 59, 56.
* Jan 27: I wrote a [runner](runner.py) that allows me to do a full search on multiple threads.
* Jan 28: 55, 54. I start the git repo.
* Jan 29: 53, 52.
* Jan 30: 51.
* Jan 31: 50, 49. Search finished.
