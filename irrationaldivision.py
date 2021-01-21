from sys import stdin, stdout
p,q = map(int,stdin.readline().strip().split())

ans = 0
if p % 2 == 1 and q % 2 == 1:
    ans = 1
elif p % 2 == 0:
    ans = 0
elif q > p:
    ans = 2

stdout.write(str(ans)+'\n')
stdout.flush()
