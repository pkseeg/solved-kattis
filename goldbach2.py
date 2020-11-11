import sys
import math
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)
n = int(lines[0])

max = 32000
primes = []
is_prime = [True] * (max+1)
for num in range(2,max+1):
    if is_prime[num]:
        primes.append(num)
        for i in range(num,max+1,num):
            is_prime[i] = False



for case in range(1,n+1):
    x = int(lines[case])
    reps = set()
    primes_sub = [num for num in primes if num < x]
    for prime in primes_sub:
        if (x - prime) in primes_sub:
            num1 = prime
            num2 = x-prime
            if num1 > num2:
                num1, num2 = num2, num1
            reps.add((num1,num2))
    reps = sorted(reps)
    print(str(x)+' has '+str(len(reps))+' representation(s)')
    for rep in reps:
        print(str(rep[0])+'+'+str(rep[1]))
    print('')
