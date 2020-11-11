import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)
t = int(lines[0])
ps = []
for i in range(1,t+1):
    l = lines[i].split(' ')
    p = float(l[1])
    ps.append(p)
ps = sorted(ps,reverse=True)
e = 0
for i in range(len(ps)):
    e += (i+1) * ps[i]
print(round(e,4))
