N = int(input())

arr = [[0] * N for _ in range(N)]
num = 1
for i in range(N):
    for j in range(N):
        arr[j][i] = num
        num += 1

for a in arr:
    print(*a)