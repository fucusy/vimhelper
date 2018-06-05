#!/usr/bin/python
import sys

previous_head = ""
first_char_count = -1
if len(sys.argv) >= 2:
    first_char_count = int(sys.argv[1])

for line in sys.stdin:
    if previous_head != line[:first_char_count]:
        previous_head = line[:first_char_count]
        print line.strip() 
