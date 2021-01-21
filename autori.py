from sys import stdin, stdout

line = stdin.readline().strip()
names = line.split('-')
ans = ''
for name in names:
	ans += name[0]
stdout.write(ans+'\n')
stdout.flush()
