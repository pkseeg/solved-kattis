import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

cards = str(lines[0])

t = 0
c = 0
g = 0
bonus = 0
for card in cards:
    if card == 'T':
        t += 1
    elif card == 'C':
        c += 1
    elif card == 'G':
        g += 1

bonus = min([t,c,g])

num = t**2 + c**2 + g**2 + (bonus * 7)
print(str(num))
