'''
START boiler plate
'''
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
'''
END boiler plate
'''
L = len('Simon says ')


lines = read_input()
n = int(lines[0])
for case in range(1,n+1):
    s = lines[case]
    if len(s) > L:
        was_simon = s[:L]
        instrct = s[L:]
        if was_simon == 'Simon says ':
            write(instrct)
finish()
