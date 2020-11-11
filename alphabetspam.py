import sys
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

s = lines[0].strip()

ws = 0
lc = 0
uc = 0
sym = 0
ttl = 0
for char in s:
    if ord(char) == 95:
        ws += 1
    elif 122 >= ord(char) >= 97:
        lc += 1
    elif 90 >= ord(char) >= 65:
        uc += 1
    else:
        sym += 1
    ttl += 1

print(ws/ttl)
print(lc/ttl)
print(uc/ttl)
print(sym/ttl)
