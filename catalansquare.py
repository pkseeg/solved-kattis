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

lines = read_input()

n = int(lines[0])
c = {0: 1}
for i in range(n+1):
    c[i+1] = c[i] * (4*i+2) // (i+2)
sys.stdout.write(str(c[n+1])+'\n')
sys.stdout.flush()
