h, m = map(int,input().split())
time = list(map(int,input().split()))

for i in range(5):
    m += time[i]

    if m > 59:
        h += int(m / 60)
        m = m % 60
    if h > 23:
        h = h % 24

print(h, m)
