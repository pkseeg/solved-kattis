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

for line in lines:
    l = [int(x) for x in line.split(' ')]
    sys.stdout.write(str(int(sum(l)/2))+'\n')
sys.stdout.flush()
