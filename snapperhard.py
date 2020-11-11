import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

t = int(lines[0])

for case in range(1,t+1):
    line = [int(x) for x in lines[case].split(' ')]
    n, k = line[0], line[1]

    # bitshift to the right
    r = ((1<<n) - 1)

    if r & k == r:
        print("Case #"+str(case)+": "+"ON")
    else:
        print("Case #"+str(case)+": "+"OFF")
