'''
read input boiler plate
'''
from sys import stdin, stdout
def read_input():
    lines = []
    for line in stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

lines = read_input()

teens = {10: 'ten',11: 'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
digits = {0: 'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

for line in lines:
    l = line.split(' ')
    should_capitalize = True
    for i, token in enumerate(l):
        if token.isdigit():
            s = ''
            t = int(token)
            tns = t // 10
            digs = t % 10
            if tns > 1:
                s += tens[tns]
                if digs != 0:
                    s += '-'+digits[digs]
            elif tns == 0:
                s += digits[digs]
            else:
                s += teens[t]

            if should_capitalize:
                s = s[0].upper()+s[1:]

            l[i] = s
            should_capitalize = False
        else:
            should_capitalize = False

    stdout.write(' '.join(l)+'\n')
