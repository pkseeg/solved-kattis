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

#from collections import Counter
import re

# functions to abstract
def type_1(s,l):
    n = len(s)
    count = 0
    for i in range(len(l)):
        if l[i:i+n] == s:
            count += 1
    return count

def type_2(s,l):
    count = 0
    seen = set()
    for i in range(len(s)):
        new_s = ''.join([s[j] for j in range(len(s)) if j != i])
        if new_s not in seen:
            count += type_1(new_s,l)
            seen.add(new_s)
    return count


def type_3(s,l):
    count = 0
    seen = set()
    for i in range(len(s)+1):
        for c in ['A','G','C','T']:
            new_s = s[:i] + c + s[i:]
            if new_s not in seen:
                count += type_1(new_s,l)
                seen.add(new_s)
    return count



lines = read_input()

for line in lines:
    if line == '0':
        break

    s,l = line.split()
    # type 1
    type1 = str(type_1(s,l))

    # type_2
    type2 = str(type_2(s,l))

    # type 3
    type3 = str(type_3(s,l))

    write(type1 + ' '+type2+' '+type3)
finish()
