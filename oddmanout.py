import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

lines = lines[1:]
cases = []
for i in range(0,len(lines),2):
    cases.append([int(lines[i]), [int(x) for x in lines[i+1].split()]])
singles = []
for case in cases:
    numbers = []
    for number in case[1]:
        if number in numbers:
            numbers.remove(number)
        else:
            numbers.append(number)
    singles.append(numbers.pop())


for i in range(len(singles)):
    print('Case #'+str(i+1)+': '+str(singles[i]))
