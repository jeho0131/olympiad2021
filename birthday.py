month = [31,28,31,30,31,30,31,31,30,31,30,31]
m, d = map(int,input().split())
bm, bd = map(int,input().split())
day = 0

if bm - m >= 2:
    for i in range(m, bm-1):
        day += month[i]

if m == bm:
    day += bd - d

else:
    day += month[m-1]-d
    day += bd

print("D-",str(day),sep='')
