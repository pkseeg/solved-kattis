# START boiler plate
from sys import stdin, stdout
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

def write(s):
    stdout.write(str(s)+'\n')

def finish():
    stdout.flush()
# END boiler plate
from collections import deque
lines = read_input()
n,s,r = map(int,lines[0].split())
teams = [1 for i in range(n)]
damaged = list(map(int,lines[1].split()))
for d in damaged:
    teams[d-1] -= 1
reserve = list(map(int,lines[2].split()))
for r in reserve:
    teams[r-1] += 1

#[1,1,1,1,1]

# special cases at the end and beginning
if teams[0] == 2 and teams[1] == 0:
    teams[0] -= 1
    teams[1] += 1
if teams[n-1] == 2 and teams[n-2] == 0:
    teams[n-1] -= 1
    teams[n-2] += 1


def count_zeros(t):
    count = 0
    for i in range(len(t)):
        if t[i] == 0:
            count += 1
    return count
# run dfs
bssf = 11
seen = set()
start = tuple(teams)
seen.add(start)
stack = deque()
stack.append(start)
while len(stack) > 0:
    t = list(stack.pop())
    bssf = min([bssf,count_zeros(t)])
    for i in range(n):
        if i > 0 and t[i] == 2 and t[i-1] == 0:
            t[i] -= 1
            t[i-1] += 1
            tup = tuple(t)
            if tup not in seen:
                stack.append(tup)
                seen.add(tup)
            t[i] += 1
            t[i-1] -= 1
        if i < n-1 and t[i] == 2 and t[i+1] == 0:
            t[i] -= 1
            t[i+1] += 1
            tup = tuple(t)
            if tup not in seen:
                stack.append(tup)
                seen.add(tup)
            t[i] += 1
            t[i+1] -= 1

write(bssf)
finish()
