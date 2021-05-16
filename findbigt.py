d = int(input())
tl = []

for i in range(d):
    tl.append([])
    for j in range(2 ** i):
        tl[i].append(int(input()))
big = 0

def findbt(y, x, num, add):
    global big
    
    if num < d:
        findbt(y+1, x*2, num+1, add+tl[y][x])
        findbt(y+1, x*2+1, num+1, add+tl[y][x])

    if num == d:
        if big < add:
            big = add

findbt(0, 0, 0, 0)

print(big)
