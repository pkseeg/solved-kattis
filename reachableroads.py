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

# this question really just asks: how many strongly connected components are there?
from collections import deque
def min_add(roads,m):
    visited = [False]*m
    nscc = 0
    for i in range(m):
        if not visited[i]:
            nscc += 1
            visited = dfs(i,visited,roads,m)
    return nscc-1

def dfs(first,visited,roads,m):
    stack = deque()
    stack.append(first)
    while len(stack) > 0:
        city = stack.pop()
        visited[city] = True
        for i in range(m):
            if not visited[i] and ((i,city) in roads or (city,i) in roads):
                stack.append(i)
    return visited

def main():
    lines = read_input()
    n = int(lines[0])
    num_cities = 0
    counter = 1
    while num_cities < n:
        num_cities += 1
        m = int(lines[counter])
        counter += 1
        r = int(lines[counter])
        counter += 1
        roads = set()
        for ep in range(counter,r+counter):
            roads.add(tuple(list(map(int,lines[ep].split()))))
        counter += r
        write(min_add(roads,m))
    finish()

main()
