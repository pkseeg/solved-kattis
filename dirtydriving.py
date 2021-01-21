from sys import stdin, stdout
lines = stdin.readlines()
n, p = map(int,lines[0].strip().split())
arr = list(map(int,lines[1].strip().split()))
arr.sort()

dist = 0

for i in range(0,len(arr)):
    should_be = p * (i + 1)
    curr = arr[i]
    dist = max(dist,should_be - curr)

ans = dist + arr[0]

stdout.write(str(ans) + '\n')
stdout.flush()
