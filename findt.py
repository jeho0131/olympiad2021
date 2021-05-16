line = list(map(int,input().split()))

bigl = 0
for i in range(3):
    if line[i] > bigl:
        bigl = line[i]

if bigl < line[0] + line[1] + line[2] - bigl:
    print("Yes")
else:
    print("No")
