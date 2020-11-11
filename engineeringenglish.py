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
seen = set()
for line in lines:
    ans = []
    words = line.split()
    for word in words:
        if word.lower() in seen:
            ans.append('.')
        else:
            ans.append(word)
            seen.add(word.lower())
    write(' '.join(ans))
finish()
