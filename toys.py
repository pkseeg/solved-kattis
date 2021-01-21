from sys import stdin, stdout
t,k = [int(x) for x in stdin.readline().strip().split()]
ans = 0
for i in range(2,t+1):
	ans = (ans + k) % i
stdout.write(str(ans)+'\n')
stdout.flush()
