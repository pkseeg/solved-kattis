import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

t = int(lines[0])

for case in range(1,t+1):
    l = [int(x) for x in lines[case].split(' ')]
    n, a, b, c, d, x0, y0, m = l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]
    points = []
    x = x0
    y = y0
    points.append((x,y))
    for i in range(1,n):
        x = (a * x + b) % m
        y = (c * y + d) % m
        points.append((x,y))
    total = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            for k in range(j+1,len(points)):
                sumx = points[i][0] + points[j][0] + points[k][0]
                sumy = points[i][1] + points[j][1] + points[k][1]
                if sumx % 3 == 0 and sumy % 3 == 0:
                    total += 1

    print('Case #'+str(case)+': '+str(total))
