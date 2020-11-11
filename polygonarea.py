import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)

# can direction be determined from the first three points alone?
i = 0
while True:
    n = int(lines[i])
    if n == 0:
        break

    i += 1
    points = []
    for j in range(n):
        points.append([int(x) for x in lines[i+j].split(' ')])

    i += n

    points.append(points[0])



    # if there are more cw than ccw, I'll go for cw
    cw = 0
    ccw = 0
    dir = ""
    theta = 0
    for j in range(0,len(points)-1,2):
        theta += (points[j+1][0]-points[j][0]) * (points[j+1][1]+points[j][1])

    if theta > 0:
        dir = "CW"
    else:
        dir = "CCW"


    a = 0
    for j in range(len(points)-1):
        a += points[j][0] * points[j+1][1] - points[j][1] * points[j+1][0]

    if a < 0:
        dir = "CW"
    else:
        dir = "CCW"
    print(dir+" "+str(abs(round(0.5*a,2))))
