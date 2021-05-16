n = int(input())
ln = list(map(int,input().split()))
m = int(input())

cl = []
def candy(add, l):
    global cl
    
    if add < m:
        for i in range(n):
            if i not in l:
                candy(add+ln[i], l + [i])
    if add == m:
        cl.append(l)

candy(0, [])
for r in range(len(cl)):
    cl[r].sort()
cl.sort()

x = 0
count = 0

while(1):
    if x >= len(cl):
        break
    x += cl.count(cl[x])
    count += 1
    
print(count)
