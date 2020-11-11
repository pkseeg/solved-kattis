import sys
from collections import Counter
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

if lines[len(lines)-1][-1] == '\n':
    lines[len(lines)-1] = lines[len(lines)-1][:-1]

for line in lines:
    s = [str(bin(ord(char)))[2:].zfill(7) for char in line.rstrip()]
    s = ''.join(s)
    count = Counter(s)
    if count['1'] % 2 == 0 and count['0'] % 2 == 0:
        print("free")
    else:
        print("trapped")
