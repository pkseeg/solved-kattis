import sys
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)


p = int(lines[0])

num = 1
for i in range(1,p+1):
    n = [int(x) for x in lines[i].split(' ')][1]

    a = 0
    b = 0
    c = 0
    odds = 0
    evens = 0
    for num in range(1,2*(n + 1)):
        if num <= n:
            a += num
        if num % 2 == 0:
            evens += 1
            if evens <= n:
                b += num
        else:
            odds += 1
            if odds <= n:
                c += num

    print(str(i)+' '+str(a)+' '+str(c)+' '+str(b))
