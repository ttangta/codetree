n = int(input())

for i in range(1, n+1):
    num = i
    for j in range(i):
        print(num, end=" ")
    print()