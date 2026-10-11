N, M = map(int, input().split())
arr = []
num = 1

for i in range(N):
    row = []
    for j in range(M):
        row.append(num)
        num+=1
    arr.append(row)

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()