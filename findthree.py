n = int(input())
nl = input().split()

l = []
for i in range(n):
    for j in range(len(nl[i])):
        if nl[i][j] == '3':
            if nl[i] not in l:
                l.append(nl[i])

l = list(map(int, l))
l.sort()
nl = list(map(int, nl))

for p in range(len(l)):
    print(str(l[p]),":",str(nl.count(l[p])), sep='')
