import math

x, y = map(int, input().split())
sj = 0

def cbreak(cx, cy, m) :
    global sj

    #초콜릿이 1개 남을 때까지 실행
    if cx > 1 or cy > 1:
        #가로의 중간을 자르는 것이 큰지 세로의 중간을 자르는 것이 큰지 비교
        if int(cx/2) * cy >= cx * int(cy/2) or cy == 1:
            
            #세종이의 차례라면 가지는 초콜릿 갯수 기록
            if m == 1:
                sj += int(cx/2) * cy
            cbreak(math.ceil(cx/2), cy, m * -1)
        
        else:
            if m == 1:
                sj += int(cy/2) * cx
            cbreak(cx, math.ceil(cy/2), m * -1)

    #초콜릿이 1개 남았을 때 세종이 차례라면 초콜릿 갯수 1 추가         
    elif m == 1:
        sj += 1

cbreak(x,y,1)
print(sj)
