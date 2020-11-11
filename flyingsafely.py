'''
read input boiler plate
'''
from sys import stdin, stdout
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

lines = read_input()

t = int(lines[0])
counter = 1
while counter < len(lines):
    n, m = [int(x) for x in lines[counter].split(' ')]
    counter += 1
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    visited = [False]*(n+1)
    for i in range(m):
        a, b = [int(x) for x in lines[counter].split(' ')]
        counter += 1

        graph[a][b] = 1
        graph[b][a] = 1

    stack = [1]
    visited[1] = True
    count = 0
    while len(stack) > 0:
        node = stack.pop(0)
        for i in range(1,len(graph)):
            if not visited[i] and graph[node][i] == 1:
                stack.append(i)
                count += 1
                visited[i] = True
    stdout.write(str(count)+'\n')
stdout.flush()
