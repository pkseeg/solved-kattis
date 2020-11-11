import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)
word = str(lines[0])

was_s = False
stop = False
for char in word:
    if char == 's' and was_s:
        print('hiss')
        stop = True
        break
    elif char == 's':
        was_s = True
    else:
        was_s = False
if not stop:
    print('no hiss')
