# START boiler plate
from sys import stdin, stdout, setrecursionlimit
x = 100000
setrecursionlimit(x)
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

def parse():
    lines = read_input()
    n,m = map(int,lines[0].split())
    owed = []
    for i in range(1,n+1):
        owed.append(int(lines[i]))

    # WE SHOULD REPRESENT FRIENDS AS A DICTIONARY
    friends = {}
    for i in range(n+1,n+1+m):
        a,b = list(map(int,lines[i].split()))
        if a not in friends:
            friends[a] = []
        if b not in friends:
            friends[b] = []
        friends[a].append(b)
        friends[b].append(a)
    return n,m,owed,friends




def main():
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        total[0] += owed[node]
        for i in friends[node]:
            if not visited[i]:
                dfs(i)


    n,m,owed,friends = parse()
    visited = [False]*n
    total = [0]
    possible = True
    for i in range(n):
        if not visited[i]:
            total = [0]
            dfs(i)
            if total[0] != 0:
                possible = False
                break
    if possible:
        write('POSSIBLE')
    else:
        write('IMPOSSIBLE')
    finish()

main()
