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

lines = read_input()
s = lines[0]
n = len(s)
n /= 3
n = int(n)
a,b,c = s[:n],s[n:2*n],s[2*n:]

if a == b or a == c:
    stdout.write(a+'\n')
elif b == c:
    stdout.write(b+'\n')
