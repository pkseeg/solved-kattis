import sys

lines = []
for line in sys.stdin:
    lines.append(line)
if lines[0] > lines[1]:
    print('no')
else:
    print('go')
