from sys import stdin, stdout
lines = stdin.readlines()
a = list(map(int,lines[0].strip()))
b = list(map(int,lines[1].strip()))
ans = ''
bns = ''
while len(a) < len(b):
	a.insert(0,0)
while len(b) < len(a):
	b.insert(0,0)
for i in range(len(a)):
	if a[i] > b[i]:
		ans += str(a[i])
	elif b[i] > a[i]:
		bns += str(b[i])
	else:
		ans += str(a[i])
		bns += str(b[i])

if ans == '':
	ans = 'YODA'
elif int(ans) == 0:
        ans = '0'
if bns == '':
	bns = 'YODA'
elif int(bns) == 0:
	bns = '0'


stdout.write(ans+'\n'+bns+'\n')
stdout.flush()
