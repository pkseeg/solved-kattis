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

deck = deque()
opn = {'(','{','['}
cls = {')','}',']'}
error = False
for i,char in enumerate(lines[1]):
    if char in opn:
        deck.append(char)
    if char in cls:
        if len(deck) == 0:
            error = True
            write(char+' '+str(i))
            break
        last = deck.pop()
        if (last == '(' and char != ')') or (last == '{' and char != '}') or (last == '[' and char != ']'):
            error = True
            write(char+' '+str(i))
            break
if not error:
    write('ok so far')
finish()
