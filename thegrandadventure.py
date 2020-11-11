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
n = int(lines[0])
items = {'$','|','*'}
for case in range(1,n+1):
    s = lines[case]
    stack = deque()
    error = False
    for char in s:
        if char in items:
            stack.append(char)
        if char == 't':
            if len(stack) == 0:
                error = True
                write('NO')
                break
            if stack.pop() != '|':
                error = True
                write('NO')
                break
        if char == 'j':
            if len(stack) == 0:
                error = True
                write('NO')
                break
            if stack.pop() != '*':
                error = True
                write('NO')
                break
        if char == 'b':
            if len(stack) == 0:
                error = True
                write('NO')
                break
            if stack.pop() != '$':
                error = True
                write('NO')
                break

    if len(stack) != 0 and not error:
        error = True
        write('NO')

    if not error:
        write('YES')

finish()
