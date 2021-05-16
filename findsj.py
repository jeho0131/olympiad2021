num = int(input())
s = input()

count = 0
for i in range(num):
    if i+1 < num:
        if s[i] == 'S' and s[i+1] == 'J':
            count += 1

print(count)
