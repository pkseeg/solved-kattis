import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)

def lcm(p,q):
    if p > q:
        g = p
    else:
        g = q

    while True:
        if g % p == 0 and g % q == 0:
            return g
        g += 1
    return -1
line = [int(x) for x in lines[0].split(' ')]
p,q,s = line[0], line[1],line[2]

if lcm(p,q) <= s:
    print('yes')
else:
    print('no')
