import math

x, y = map(int, input().split())
sj = 0

def cbreak(cx, cy, m) :
    global sj

    if cx > 1 or cy > 1:
        if int(cx/2) * cy >= cx * int(cy/2) or cy == 1:
            if m == 1:
                sj += int(cx/2) * cy
            cbreak(math.ceil(cx/2), cy, m * -1)

        else:
            if m == 1:
                sj += int(cy/2) * cx
            cbreak(cx, math.ceil(cy/2), m * -1)
                
    elif m == 1:
        sj += 1

cbreak(x,y,1)
print(sj)
