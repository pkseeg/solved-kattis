import sys
import math

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

num_cases = int(lines[0])
for i in range(1,num_cases+1):
    nldg = [int(x) for x in lines[i].split()]
    n = nldg[0]
    l = nldg[1]
    d = nldg[2]
    g = nldg[3]


    perimeter = l * n
    apothem = (l)/(2 * math.tan(math.pi/n))
    area = (1/2) * perimeter * apothem

    side1 = d * g
    side2 = l
    rectangles = side1 * side2 * n

    r = d * g
    circle = math.pi * r**2

    area += rectangles + circle


    print(area)
