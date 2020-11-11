import sys
import heapq
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

n = int(lines[0])

queue = []
max_x = 0
for case in range(1,n+1):
    l = [int(x) for x in lines[case].split(' ')]
    heapq.heappush(queue,(l[0],l[1],l[2]))
    if l[2] > max_x:
        max_x = l[2]


floor = [0]*(max_x+1)
length = 0
while len(queue) > 0:
    plt = heapq.heappop(queue)

    y = plt[0]
    x1 = plt[1]
    x2 = plt[2]

    length += (y - floor[x1+1])
    length += (y - floor[x2])

    for space in range(x1+1,x2+1):
        if floor[space] <= y:
            floor[space] = y

print(length)
