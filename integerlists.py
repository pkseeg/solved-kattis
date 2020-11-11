'''
read input boiler plate
'''
from sys import stdin, stdout
from collections import deque
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

lines = read_input()

num_tests = int(lines[0])

for case in range(1,3*num_tests+1,3):
    # get the input
    p = lines[case]
    n = int(lines[case+1])
    if n > 0:
        lst = deque([int(x) for x in lines[case+2][1:len(lines[case+2])-1].split(',')])
    else:
        lst = deque([])

    # we start going forward through the input list
    forward = True
    error = False
    for c in p:
        if c == 'R':
            forward = not forward
        else:
            if len(lst) > 0:
                if forward:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                error = True
                break

    if error:
        stdout.write('error\n')
    else:
        stdout.write('[')
        if forward:
            for i, num in enumerate(lst):
                stdout.write(str(num))
                if i < len(lst)-1:
                    stdout.write(',')
        else:
            for i in range(len(lst)-1,-1,-1):
                stdout.write(str(lst[i]))
                if i > 0:
                    stdout.write(',')
        stdout.write(']\n')
