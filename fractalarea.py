def frac_area(r,i,n):
    if i > n:
        return
    else:
        return

import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)

t = int(lines[0])
pi = 3.141592653589793
for case in range(1,t+1):
    line = [int(x) for x in lines[case].split(' ')]
    r = line[0]
    n = line[1]

    # first iteration
    a = pi*r*r

    if n == 1:
        print(a)
        continue

    r /= 2
    # second iteration
    a += (4 * pi * r * r)
    if n == 2:
        print(a)
        continue


    # for every iteration afterwards
    num_circles = 4
    for i in range(3,n+1):
        r /= 2
        a += ((3 * pi * r * r)*num_circles)
        num_circles *= 3

    print(a)
