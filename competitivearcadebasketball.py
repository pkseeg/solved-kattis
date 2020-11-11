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

n,p,m = map(int,lines[0].split())
contestants = {}
for con in range(1,n+1):
    contestants[lines[con]] = 0
winnerfound = False
winners = set()
for s in range(1+n,m+n+1):
    con, score = lines[s].split()
    score = int(score)
    contestants[con] += score
    if contestants[con] >= p and con not in winners:
        write(con+' wins!')
        winners.add(con)
        winnerfound = True
if not winnerfound:
    write('No winner!')
finish()
