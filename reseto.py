import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)
line = [int(x) for x in lines[0].split(' ')]
n, k = line[0],line[1]

crossed = 0
is_prime = [True]*(n+1)
is_prime[0] = False
is_prime[1] = False
should_stop = False

for num in range(2,n+1):
    if is_prime[num]==True:
        is_prime[num] = False
        crossed += 1
        if crossed == k:
            print(num)
            break
        r = n // num
        for i in range(2,r+1):
            if is_prime[num*i]:
                is_prime[num*i] = False
                crossed += 1
                if crossed == k:
                    print(num*i)
                    should_stop = True
                    break
    if should_stop:
        break
