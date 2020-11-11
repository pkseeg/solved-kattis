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
total = 0
for case in range(1,len(lines)):
    x,y = [float(x) for x in lines[case].split()]
    total += x * y
write(total)
finish()
