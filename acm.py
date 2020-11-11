import sys
lines = []
for line in sys.stdin:
    if '-1' == line.rstrip():
        break
    lines.append(line)

'''
7 H right
15 B wrong
30 E wrong
35 E right
80 B wrong
80 B right
100 D wrong
100 C wrong
300 C right
300 D wrong
This team solved 4 problems, and their total time score (including penalties) is
502, with 7 minutes for H, 35+20 for E, 80+40 for B, and 300+20 for C.
'''

num_solved = 0
time_score = 0
attempted = {}
for l in lines:
    line = [x for x in l.split()]

    time = int(line[0])

    prob = line[1]
    if prob in attempted:
        attempted[prob] += 1
    else:
        attempted[prob] = 0

    if line[2]=="right":
        num_solved += 1
        time_score += time
        if attempted[prob] > 0:
            time_score += attempted[prob] * 20
if num_solved == 0:
    print("0 0")
else:
    print(str(num_solved) +" "+ str(time_score))
