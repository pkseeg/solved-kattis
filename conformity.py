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

n = int(lines[0])
map = {}

for i in range(1,n+1):
    s = frozenset(lines[i].split())
    if s in map:
        map[s] += 1
    else:
        map[s] = 1

maxp = -1
for k in map:
    if map[k] > maxp:
        maxp = map[k]

most_pop = 0
for k in map:
    if map[k] == maxp:
        most_pop += map[k]

write(most_pop)
finish()
