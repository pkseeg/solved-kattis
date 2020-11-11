import sys
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)



for i in range(0,len(lines),3):
    nx = int(lines[i].split(' ')[0])
    ny = int(lines[i].split(' ')[1])
    w = float(lines[i].split(' ')[2])

    if nx == 0 and ny == 0 and w == 0.0:
        break

    last = 0.0
    shouldContinue = True

    xlist = sorted([float(a) for a in lines[i+1].split(' ')])
    ylist = sorted([float(a) for a in lines[i+2].split(' ')])

    if xlist[-1] < 75.0-w/2:
        print('NO')
        shouldContinue = False
        continue

    if ylist[-1] < 100.0-w/2:
        print('NO')
        shouldContinue = False
        continue


    if nx > 0:
        for x in xlist:
            if x - last > w:
                print('NO')
                shouldContinue = False
                break
            else:
                last = x

    if ny > 0:
        if shouldContinue:
            last = 0.0
            for y in ylist:
                if y - last > w:
                    print('NO')
                    shouldContinue = False
                    break
                else:
                    last = y

    if shouldContinue:
        print('YES')
