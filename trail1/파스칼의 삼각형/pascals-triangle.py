N = int(input())

arr = [[0] * N for _ in range(N)]

arr[0][0] = 1
for i in range(1, N):
    for j in range(i+1):
        r1 = i-1
        c1 = j-1
        if c1 < 0:
            arr[i][j] = 0
        else:
            arr[i][j] = arr[r1][c1]
        arr[i][j] += arr[i-1][j]

for i in range(N):
    a = arr[i]
    for j in range(N):
        if a[j] == 0:break
        print(a[j], end = " ")
    print()