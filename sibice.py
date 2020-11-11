import sys
import math

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

n = int(lines[0].split()[0])
w = int(lines[0].split()[1])
h = int(lines[0].split()[2])
bottom = math.sqrt(w**2 + h**2)

for i in range(1,n+1):
    match = int(lines[i])
    if match <= bottom:
        print("DA")
    else:
        print("NE")
