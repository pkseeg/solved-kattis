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

keys = {'1':['1','2','3','4','5','6','7','8','9','0'],'2':['2','5','3','8','6','9','0'],'3':['3','6','9'],'4':['4','5','6','7','8','9','0'],'5':['5','6','8','9','0'],'6':['9','6'],'7':['8','0','9','7'],'8':['0','9','8'],'9':['9'],'0':['0']}
def can_get(num):
    for i in range(len(num)-1):
        if num[i+1] not in keys[num[i]]:
            return False
    return True
lines = read_input()
t = int(lines[0])
for case in range(1,t+1):
    num = lines[case]
    if can_get(num):
        write(num)
        continue
    hi = int(num)+1
    lo = int(num)-1
    while True:
        if can_get(str(hi)):
            write(hi)
            break
        elif can_get(str(lo)):
            write(lo)
            break
        hi += 1
        lo -= 1
finish()
