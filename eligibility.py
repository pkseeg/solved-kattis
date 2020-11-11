import sys

lines = []
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)

num = int(lines[0])
def date_to_num(year,month,day):
    return 10000*year + 100*month + day

student_info = []
for i in range(1,num+1):
    name = lines[i].split()[0]
    ps = lines[i].split()[1]
    ps = date_to_num(int(ps[:4]),int(ps[5:7]),int(ps[8:]))
    birth = lines[i].split()[2]
    birth = date_to_num(int(birth[:4]),int(birth[5:7]),int(birth[8:]))
    num_courses = int(lines[i].split()[3])
    student_info.append((name,ps,birth,num_courses))


ps_mark = date_to_num(2010, 0, 0)
birth_mark = date_to_num(1991, 0, 0)
course_mark = 40

def is_eligible(student):
    if student[1] >= ps_mark or student[2] >= birth_mark:
        return "eligible"
    elif student[3] > course_mark:
        return "ineligible"
    else:
        return "coach petitions"

for student in student_info:
        print(student[0]+" "+is_eligible(student))
