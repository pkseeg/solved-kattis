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

lines = read_input()
# get dimensions
m,n = map(int,lines[0].split())
def valid(r,c):
    return 0 <= r < m and 0 <= c < n
# get matrix
matrix = [['' for i in range(n)] for j in range(m)]
for r in range(1,m+1):
    for c in range(n):
        matrix[r-1][c] = lines[r][c]

all_visited = [[False for i in range(n)] for j in range(m)]
moves = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
from collections import deque
def dfs(r,c):
    stack = deque()
    stack.append((r,c))
    while len(stack) > 0:
        r_,c_ = stack.pop()
        all_visited[r_][c_] = True
        for r_m,c_m in moves:
            if valid(r_+r_m,c_+c_m) and not all_visited[r_+r_m][c_+c_m] and matrix[r_+r_m][c_+c_m] == '#':
                stack.append((r_+r_m,c_+c_m))

num_loops = 0
for r in range(m):
    for c in range(n):
        if not all_visited[r][c] and matrix[r][c] == '#':
            all_visited[r][c] = True
            dfs(r,c)
            num_loops += 1
write(num_loops)
finish()
