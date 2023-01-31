#!/usr/bin/env python3
from verify import levtopmn
import sys
print(*levtopmn(int(sys.argv[1])), sep='\n')
