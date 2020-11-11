import sys
s = sys.stdin.readline()

stack = []

for char in s:
    if char == '<':
        stack.pop()
    else:
        stack.append(char)

print(''.join(stack))
