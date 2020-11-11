'''
read input boiler plate
'''
from sys import stdin, stdout
import string
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

lines = read_input()




s = lines[0].split(' ')


def is_umm(token):
    token = token.translate(str.maketrans('', '', string.punctuation))
    return len(token) == token.count('u')+token.count('m')


s = ''.join([char for char in s if is_umm(char)])


def to_binary(s_new):
    b = ['']*len(s_new)
    for i,char in enumerate(s_new):
        if char == 'm':
            b[i] = '0'
        elif char == 'u':
            b[i] = ('1')
    return ''.join(b)

b = to_binary(s)

splits = []
for i in range(0,len(b),7):
    splits.append(b[i:i+7])


stdout.write(''.join([chr(int(split,2)) for split in splits])+'\n')
stdout.flush()
