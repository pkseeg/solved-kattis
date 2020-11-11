import sys
from collections import Counter
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

t = int(lines[0])

for case in range(1,t+1):
    m = 0
    for i in range(1,len(lines[case])):
        s = str(bin(int(lines[case][:i])))
        count = Counter(s)
        m = max(m,count['1'])
    print(m)
