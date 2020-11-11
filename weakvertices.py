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


def found_triangle(k, adj):
    for i in range(len(adj)):
        if adj[k][i] == '1':
            for j in range(i+1,len(adj)):
                if adj[k][j] == '1' and adj[i][j] == '1':
                    return True
    return False

lines = read_input()

counter = 0
while counter < len(lines):
    n = int(lines[counter])
    if n == -1:
        break
    counter += 1

    adj = [[0 for i in range(n)] for j in range(n)]
    for i in range(counter,n+counter):
        l = lines[i].split(' ')
        for j,a in enumerate(l):
            adj[i-counter][j] = a
    counter += n


    # okay so here is where we determine the weak points
    for i in range(n):
        if found_triangle(i,adj):
            continue
        else:
            stdout.write(str(i)+' ')
    stdout.write('\n')
stdout.flush()
