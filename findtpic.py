n = int(input())

m = []
for i in range(n):
    m.append(input())

count = 0
def findload(num, x, y, l, bxy):
    global count
    ll = l[:]
    
    if m[y][x] == 'T' and ll[0] != 1:
        bxy = [0,0]
        ll[0] = 1
    if m[y][x] == 'G' and ll[0] == 1:
        ll[1] = 1

    if (0 in l and not(x == 1 and y == 1)) or num == 0:
        print(x, y)
        
        if m[y-1][x] != '#' and not(y-1 == bxy[1] and x == bxy[0]):
            findload(num+1, x, y-1, ll, [x,y])
        if m[y][x-1] != '#' and not(y == bxy[1] and x-1 == bxy[0]):
            findload(num+1, x-1, y, ll, [x,y])
        if m[y+1][x] != '#' and not(y+1 == bxy[1] and x == bxy[0]):
            findload(num+1, x, y+1, ll, [x,y])
        if m[y][x+1] != '#' and not(y == bxy[1] and x+1 == bxy[0]):
            findload(num+1, x+1, y, ll, [x,y])
            
    if 0 not in ll:
        if count > num or count == 0:
            count = num

for i in range(n):
    for j in range(n):
        if m[i][j] == 'S':
            findload(0, j, i, [0,0], [0,0])

print(count)
