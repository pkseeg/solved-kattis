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

d = {}
for i in range(1,len(lines)):
    if lines[i] in d:
        d[lines[i]] += 1
    else:
        d[lines[i]] = 1

min = 100000000000
min_vals = []
for k in d:
    if d[k] < min:
        min_vals.clear()
        min_vals.append(k)
        min = d[k]
    elif d[k] == min:
        min_vals.append(k)

min_vals.sort()
for costume in min_vals:
    write(costume)
finish()
