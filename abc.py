import sys
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

nums = [int(x) for x in lines[0].split()]
string = lines[1]

ordered = []
for loop in range(3):
    min_num = min(nums)
    ordered.append(min_num)
    nums.remove(min_num)

ret = ''
for char in string:
    if char == 'A':
        ret += str(ordered[0]) + ' '
    elif char == 'B':
        ret += str(ordered[1]) + ' '
    elif char == 'C':
        ret += str(ordered[2]) + ' '

ret = ret[:len(ret)-1]
print(ret)
