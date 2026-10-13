N = int(input())

arr = [[0] * N for _ in range(N)]

for i in range(N):
    arr[0][i] = 1
    arr[i][0] = 1

for i in range(1, N):
    for j in range(1, N):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]
        
for a in arr:
    print(*a)