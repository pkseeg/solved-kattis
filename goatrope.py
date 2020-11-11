import sys
import math

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

line = [float(int(x)) for x in lines[0].split()]

x = line[0]
y = line[1]
x1 = line[2]
y1 = line[3]
x2 = line[4]
y2 = line[5]

def dist(x,y,x1,y1):
    return math.sqrt((y1-y)**2 + (x1-x)**2)

# there are 8 cases, in my head
if x < x1:
    if y < y1:
        print(dist(x,y,x1,y1))
    elif y1 < y and y < y2:
        print(dist(x,y,x1,y))
    elif y2 < y:
        print(dist(x,y,x1,y2))
elif x1 < x and x < x2:
    if y < y1:
        print(dist(x,y,x,y1))
    elif y2 < y:
        print(dist(x,y,x,y2))
elif x2 < x:
    if y < y1:
        print(dist(x,y,x2,y1))
    elif y1 < y and y < y2:
        print(dist(x,y,x2,y))
    elif y2 < y:
        print(dist(x,y,x2,y2))
