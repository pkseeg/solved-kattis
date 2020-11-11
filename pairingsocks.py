'''
read input boiler plate
'''
import sys
def read_input():
    lines = []
    for line in sys.stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

from collections import deque

lines = read_input()

n = int(lines[0])
pile = [int(x) for x in lines[1].split(' ')]

q = deque()

moves = 0
while len(pile) > 0:
    moves += 1
    if len(q) == 0:
        q.append(pile.pop())
    elif pile[-1] == q[-1]:
        pile.pop()
        q.pop()
    else:
        q.append(pile.pop())
if len(q) != 0:
    sys.stdout.write('impossible\n')
else:
    sys.stdout.write(str(moves)+'\n')
sys.stdout.flush()
