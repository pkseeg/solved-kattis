import sys
s = sys.stdin.readline()

d = {}
d['a'] = '@'
d['b'] = '8'
d['c'] = '('
d['d'] = '|)'
d['e'] = '3'
d['f'] = '#'
d['g'] = '6'
d['h'] = '[-]'
d['i'] = '|'
d['j'] = '_|'
d['k'] = '|<'
d['l'] = '1'
d['m'] = '[]\\/[]'
d['n'] = '[]\\[]'
d['o'] = '0'
d['p'] = '|D'
d['q'] = '(,)'
d['r'] = '|Z'
d['s'] = '$'
d['t'] = "']['"
d['u'] = '|_|'
d['v'] = '\\/'
d['w'] = '\\/\\/'
d['x'] = '}{'
d['y'] = '`/'
d['z'] = '2'

ans = ''
for char in s:
    if char.lower() in d:
        ans += d[char.lower()]
    else:
        ans += char
print(ans)
