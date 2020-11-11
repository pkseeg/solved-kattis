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
a = list(map(int,lines[1].split()))
floor = a[0]
ans = [a[0]]
for num in a:
    if num > floor:
        ans.append(num)
        floor = num
write(len(ans))
write(' '.join([str(x) for x in ans]))
finish()
