n = int(input())
p = list(map(int,input().split()))

count = 0
for i in range(10):
    if p[i] >= n:
        count += 1

print(count)
