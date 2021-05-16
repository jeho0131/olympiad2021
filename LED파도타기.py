abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
       'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t, cn = map(int,input().split())
l = abc[:cn] + ['0']

def b(n,m):
    if n >= 0:
        print(l[int(m / ((cn+1) ** n))-1],end='')
        b(n-1, m % ((cn + 1) ** n))

a = 0
while(1):
    if t < (cn+1) ** a:
        a -= 1
        break
    a += 1

b(a, t)
