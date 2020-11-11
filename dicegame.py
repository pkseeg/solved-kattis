import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

gunnar_dice = [int(x) for x in lines[0].split()]
emma_dice = [int(x) for x in lines[1].split()]

gunnar_expected = sum([i for i in range(gunnar_dice[0],gunnar_dice[1])])/(gunnar_dice[1] - gunnar_dice[0]) + sum([i for i in range(gunnar_dice[2],gunnar_dice[3])])/(gunnar_dice[3] - gunnar_dice[2])
emma_expected = sum([i for i in range(emma_dice[0],emma_dice[1])])/(emma_dice[1] - emma_dice[0]) + sum([i for i in range(emma_dice[2],emma_dice[3])])/(emma_dice[3] - emma_dice[2])

if gunnar_expected > emma_expected:
    print('Gunnar')
elif emma_expected > gunnar_expected:
    print('Emma')
else:
    print('Tie')
