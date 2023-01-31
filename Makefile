CXXFLAGS=-O2
shortsphere: shortsphere.cc
graph.png: dot.py
	./dot.py | dot -Tpng > graph.png
	if which pngcrush >/dev/null; then \
		mv graph.png graph.tmp.png; \
		pngcrush -rem alla -rem text -reduce -brute -l 9 graph.tmp.png graph.png; \
		$(RM) graph.tmp.png; \
	fi
