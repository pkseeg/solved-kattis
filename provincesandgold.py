import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

g = int(lines[0].split()[0])
s = int(lines[0].split()[1])
c = int(lines[0].split()[2])

points = 3 * g + 2 * s + 1 * c

noVic = False
st = ""
if points >= 8:
    st += "Province"
elif points >= 5:
    st += "Duchy"
elif points >= 2:
    st += "Estate"
else:
    noVic = True
if not noVic:
    st += " or "
if points >= 6:
    st += "Gold"
elif points >= 3:
    st += "Silver"
else:
    st += "Copper"

print(st)
