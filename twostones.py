from sys import stdin, stdout

n = int(stdin.readline())
ans = ''
if n % 2 == 1:
	ans = 'Alice\n'
else:
	ans = 'Bob\n'
stdout.write(ans)
stdout.flush()
