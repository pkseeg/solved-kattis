import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

max_people = int(lines[0].split()[0])
x = int(lines[0].split()[1])

total_people = 0
num_rejections = 0
for i in range(1,x+1):
    event = lines[i].split()[0]
    size = int(lines[i].split()[1])
    if event == "enter":
        if total_people + size > max_people:
            num_rejections += 1
        else:
            total_people += size
    if event == "leave":
        total_people -= size

print(num_rejections)
