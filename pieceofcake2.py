import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

nums = [int(x) for x in lines[0].split()]

n = nums[0]
h = nums[1]
v = nums[2]

height = max([n-h,h])
width = max([n-v,v])

print(width*height*4)
