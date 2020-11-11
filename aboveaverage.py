'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''
import sys
lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

n = int(lines[0])

for case in range(1,n+1):
    num_students = [int(x) for x in lines[case].split()][0]
    scores = [int(x) for x in lines[case].split()][1:]
    sum_scores = 0
    for score in scores:
        sum_scores += score
    mean_score = sum_scores/num_students
    total_above = 0
    for score in scores:
        if score > mean_score:
            total_above += 1
    # "%.2f" % round(a, 2)
    print("%.3f" % round(total_above/num_students*100,3)+"%")
    #print(str(round(total_above/num_students*100,3)) + '%')
