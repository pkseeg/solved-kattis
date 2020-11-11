import sys

ints = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    ints.append(int(line))

# return the number of unique nums mod 42
unique = set()
for num in ints:
    unique.add(num % 42)
print(len(unique))
