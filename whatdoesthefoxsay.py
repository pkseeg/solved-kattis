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
n = int(lines[0])
it = 1
for case in range(n):
    line = lines[it].split(' ')
    it += 1

    noises = set()

    s = lines[it].split(' ')
    it += 1

    while len(s) == 3:
        noises.add(s[2])
        s = lines[it].split(' ')
        it += 1

    p = ''
    for l in line:
        if l not in noises:
            p += l + ' '
    p = p[:-1]
    stdout.write(p+'\n')
