class fenwick_tree:
    def __init__(self,n):
        self.arr = [0]*(n+1)
        self.diff_arr = [0]*n

    def update(self,ind,val):
        diff = val - self.diff_arr[ind]
        self.diff_arr[ind] = val
        nxt = ind+1
        while nxt < len(self.arr):
            self.arr[nxt] += diff
            nxt = nxt + (nxt & (-nxt))

    def increment(self,ind,val):
        nxt = ind+1
        while nxt < len(self.arr):
            self.arr[nxt] += val
            nxt = nxt + (nxt & (-nxt))

    def getsum(self,ind):
        s = 0
        cur = ind+1
        while cur > 0:
            s += self.arr[cur]
            cur = cur & (cur-1)
        return s

    def __str__(self):
        return str(self.arr)


import sys
lines = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    lines.append(line)

n,q = [int(x) for x in lines[0].split(' ')]
tree = fenwick_tree(n)
for i in range(1,q+1):
    l = lines[i].split(' ')
    if l[0] == '+':
        tree.increment(int(l[1]),int(l[2]))
    else:
        sys.stdout.write(str(tree.getsum(int(l[1])-1))+'\n')
sys.stdout.flush()
