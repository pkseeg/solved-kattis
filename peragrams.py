import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

inputStr = lines[0].rstrip()

# minimun number of letters removed so that it becomes a peragram
# peragram is basically just any character needs to be there twice, except one
wordSet = set()
for char in inputStr:
    if char in wordSet:
        wordSet.remove(char)
    else:
        wordSet.add(char)


if len(wordSet) > 0:
    print(len(wordSet)-1)
else:
    print("0")
