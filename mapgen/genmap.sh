#!/bin/sh
genmap1() {
	montage \
		-geometry 160x160+0+0 \
		-background black \
		-tile 2x \
		$(printf 'img/%03d-c.png img/%03d-a.png img/%03d-d.png img/%03d-b.png' $3 $1 $4 $2) \
		png:-
}
genmap() {
	genmap1 $(../getpatterns.py $1)
}
optimize() {
	if which pngcrush >/dev/null; then \
		mv $1 ${1%.png}.tmp.png
		pngcrush -rem alla -rem text -reduce -brute -l 9 ${1%.png}.tmp.png $1
		rm -f ${1%.png}.tmp.png
	fi
}
for i in \
	001 011 012 013 022 023 032 033 034 \
	035 045 046 056 057 067 068 078 079 \
	080 081 090 091 092 093 103 113 114 \
	115 125 126 136 146 156 157 167 177 \
	178 188 189 199 200 210 211 212 221 \
	222 223 224 234 235 236 245 246 255 \
	256
do
	genmap $i > out/$i.png
	optimize out/$i.png
done
