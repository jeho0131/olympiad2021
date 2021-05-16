n, r = map(int,input().split())
n = str(n)

nn = [0 for i in range(len(n))]
rr = abs(r) % len(n)

for i in range(len(n)):
    if r > 0:
        if len(n)-1 < i + rr:
            nn[(i+rr)%len(n)] = n[i]
        else:
            nn[i+rr] = n[i]
            
    elif r == 0:
        nn[i] = n[i]

    elif r < 0:
        if 0 > i - rr:
            nn[(i-rr)+len(n)] = n[i]
        else:
            nn[i-rr] = n[i]
            
for i in range(len(nn)):
    print(nn[i],end='')
