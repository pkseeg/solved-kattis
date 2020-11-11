import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

e = int(lines[0].split()[0])
f = int(lines[0].split()[1])
c = int(lines[0].split()[2])

total_bottles = e + f
drank = 0
while total_bottles >= c:
    total_bottles -= c
    total_bottles += 1
    drank += 1

print(drank)
