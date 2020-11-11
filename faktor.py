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

a, i = [int(x) for x in lines[0].split(' ')]

sys.stdout.write(str((i-1)*a+1)+'\n')
sys.stdout.flush()
