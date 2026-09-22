n = int(input())

for i in range(1, n+1):
    row = i
    for j in range(1, i+1):
        print(row * j, end = " ")
    print()