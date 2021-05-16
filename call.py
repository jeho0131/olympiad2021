n = int(input())

f = []
for i in range(n):
    f.append(list(map(int,input().split())))

l = [0 for i in range(n)]
al = []

count = 0

def findf(num):
    global l
    
    for i in range(n):
        if (f[num][i] == 1 and l[i] != 1) and i != num:
            l[i] = 1
            findf(i)

def addl(nl,ol,num):
    pl = []
    cnl = nl[:]
    
    for i in range(n):
        if nl[i] == 0:
            cnl = nl[:]
            cnl[i] = 1
            for j in range(n):
                if al[i][j] == 1 or ol[j] == 1:
                    pl.append(1)
                else:
                    pl.append(0)
                    
            addl(nl,pl,num+1)

    if 0 not in l:
        if count > num or count == 0:
            count = num

for i in range(n):
    findf(i)
    al.append(l)
    l = [0 for k in range(n)]

ll = [0 for i in range(n)]
addl(ll,ll,0)

print(count)
