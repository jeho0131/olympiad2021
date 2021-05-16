n = int(input())

an = 2
bn = 1
add = 0

for i in range(n):
    add += an
    an, bn = an+bn, an
print(add)
