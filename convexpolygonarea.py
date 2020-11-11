'''
BOILER PLATE COMP GEOM
'''
import math

INF = 1*10**100
EPS = 1*10**-20

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,o):
        return point(self.x + o.x,self.y+o.y)

    def __sub__(self,o):
        return point(self.x-o.x,self.y-o.y)

    def __mul__(self,c):
        return point(self.x*c,self.y*c)

    def __truediv__(self,c):
        return point(self.x/c.self.y/c)

    def __floordiv__(self,c):
        return point(self.x//c,self.y//c)

    def __str__(self):
        return 'x: '+str(self.x)+' y: '+str(self.y)

def dot(p,q):
    return p.x*q.x + p.y*q.y
def dist(p,q):
    return math.sqrt(dot(p-q,p-q))
def cross(p,q):
    return p.x*q.y - p.y*q.x
def segments_parallel(a,b,c,d):
    return abs(cross(a-b,c-d)) < EPS

def point_on_segment(p,a,b):
    if dist(p,a) < EPS:
        return True
    if dist(p,b) < EPS:
        return True
    if segments_parallel(p,a,p,b) and dot(p-a,p-b) < 0:
        return True
    return False

def point_in_polygon(p,a):
    c = False
    for i in range(len(a)):
        j = (i+1) % (len(a))
        if (p.y < a[i].y != p.y < a[j].y) and (p.x < a[i].x + (a[j].x-a[i].x)*(p.y-a[i].y)/(a[j].y-a[i].y)):
            c = not c
    return c

def point_on_polygon(p,pgn):
    for i in range(len(pgn)-1):
        if point_on_segment(p,pgn[i],pgn[(i+1)%len(pgn)]):
            return True
    return False

def signed_area(a):
    area = 0
    for i in range(len(a)):
        j = (i+1) % len(a)
        area += cross(a[i],a[j])
    return area/2.0




'''
read input boiler plate
'''
import sys
def read_input():
    lines = []
    for line in sys.stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines



lines = read_input()
n = int(lines[0])

for case in range(1,n+1):
    line = [int(x) for x in lines[case].split(' ')]
    m = line[0]
    polygon = []
    for i in range(1,2*m+1,2):
        q = point(line[i],line[i+1])
        polygon.append(q)
    area = signed_area(polygon)
    if area.is_integer(): sys.stdout.write(str(int(area))+'\n')
    else: sys.stdout.write(str(area)+'\n')
sys.stdout.flush()
