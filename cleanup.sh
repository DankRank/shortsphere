#!/bin/sh
for i in out/*.txt; do
	if [ ! -s $i ]; then
		x=${i#out/}
		x=${x%.txt}
		echo $x >> empty.txt
		rm $i
	fi
done
