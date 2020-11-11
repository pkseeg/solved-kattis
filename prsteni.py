import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip().lower():
        break
    lines.append(line)

def gcd(first, next):
    if first == 0:
        return next
    return gcd(next%first, first)

n = int(lines[0])
rings = [int(x) for x in lines[1].split(' ')]

first = rings[0]
for i in range(1,n):
    next = rings[i]
    # find greatest common denominator of first and next
    denom = gcd(first,next)
    print(str(first // denom)+"/"+str(next // denom))
