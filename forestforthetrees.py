# START boiler plate
from sys import stdin, stdout
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

def write(s):
    stdout.write(str(s)+'\n')

def finish():
    stdout.flush()
# END boiler plate
def gcd(x,y):
    a,b = x,y
    while b > 0:
        a,b = b, a % b
    return a

def reduce(x,y,g):
    return x//g, y//g

def cleared(px,py):
    if px == 0 and py == 0:
        return True
    return x1 <= px <= x2 and y1 <= py <= y2

def main(bx,by,x1,y1,x2,y2):
    g = gcd(bx,by)
    xr, yr = reduce(bx,by,g)
    if g == 1:
        write('Yes')
        return

    if not cleared(xr,yr):
        write('No')
        write(str(xr)+' '+str(yr))
        return

    lo = 1
    hi = g
    ans = [-1,-1]
    can_see = True
    while lo+1 < hi:
        mid = (lo+hi) // 2
        if not cleared(xr*mid,yr*mid):
            can_see = False
            ans = [xr*mid,yr*mid]
            hi = mid
        else:
            lo = mid

    if can_see:
        write('Yes')
        return
    else:
        write('No')
        write(str(ans[0])+' '+str(ans[1]))
        return




lines = read_input()
bx, by = [int(x) for x in lines[0].split()]
x1,y1,x2,y2 = [int(x) for x in lines[1].split()]
main(bx, by, x1, y1, x2, y2)
finish()
