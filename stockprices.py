'''
read input boiler plate
'''
import sys
import heapq
def read_input():
    lines = []
    for line in sys.stdin:
        if 'exit' == line.lower().rstrip():
            break
        lines.append(line.rstrip())
    return lines

lines = read_input()
it = 1
while it < len(lines):
    n = int(lines[it])
    it += 1

    temp = -1
    # define my priority queues
    buy = []
    sell = []

    for i in range(it,n+it):
        l = lines[it].split(' ')
        it += 1

        # grab the num and the price
        num = int(l[1])
        price = int(l[4])


        if l[0] == 'buy':
            heapq.heappush(buy,(-1*price,num))
        else:
            heapq.heappush(sell,(price,num))

        while(len(buy) > 0 and len(sell) > 0):
            b = buy[0]
            s = sell[0]

            if -1*b[0] < s[0]:
                break

            temp = s[0]
            heapq.heappop(buy)
            heapq.heappop(sell)
            if b[1] < s[1]:
                heapq.heappush(sell,(s[0],s[1]-b[1]))
            elif b[1] > s[1]:
                heapq.heappush(buy,(b[0],b[1]-s[1]))
        if len(sell) == 0:
            sys.stdout.write('- ')
        else:
            sys.stdout.write(str(sell[0][0])+' ')

        if len(buy) == 0:
            sys.stdout.write('- ')
        else:
            sys.stdout.write(str(-1*buy[0][0])+' ')

        if temp == -1:
            sys.stdout.write('-\n')
        else:
            sys.stdout.write(str(temp)+'\n')

sys.stdout.flush()
