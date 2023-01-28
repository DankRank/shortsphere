#!/bin/sh
cat out/*.txt | cut -d' ' -f1 | sort -nu
