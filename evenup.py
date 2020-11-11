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

cards = [int(x) for x in lines[1].split(' ')]

queue = deque()
queue.append(cards[0])
for i in range(1,len(cards)):
    if len(queue) != 0:
        if cards[i] % 2 == queue[-1]%2:
            queue.pop()
        else:
            queue.append(cards[i])
    else:
        queue.append(cards[i])

sys.stdout.write(str(len(queue))+'\n')
sys.stdout.flush()
