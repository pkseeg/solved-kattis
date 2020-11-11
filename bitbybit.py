import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

def clear(i,s):
    s[i] = '0'
    return s

def set(i,s):
    s[i] = '1'
    return s

def aand(i,j,s):
    if s[i] == '1' and s[j] == '1':
        s[i] = '1'
    elif s[i] == '0' or s[j] == '0':
        s[i] = '0'
    else:
        s[i] = '?'
    return s

def oor(i,j,s):
    if s[i] == '1' or s[j] == '1':
        s[i] = '1'
    elif s[i] == '0' and s[j] == '0':
        s[i] = '0'
    else:
        s[i] = '?'
    return s


n = int(lines[0])
i = 1
while n != 0:
    s = ["?"]*32
    for j in range(i,n+i):
        i += 1
        line = lines[j].split(' ')
        c = line[0]

        if c == "CLEAR":
            s = clear(int(line[1]),s)
        elif c == "SET":
            s = set(int(line[1]),s)
        elif c == "OR":
            s = oor(int(line[1]),int(line[2]),s)
        elif c == "AND":
            s = aand(int(line[1]),int(line[2]),s)
    s.reverse()
    print(''.join(s))
    n = int(lines[i])
    i += 1
