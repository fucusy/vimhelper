#!/usr/bin/python
import sys
import random

all_lines = []
for line in sys.stdin:
    all_lines.append(line.rstrip('\n'))

random.shuffle(all_lines)

for line in all_lines:
    print line
