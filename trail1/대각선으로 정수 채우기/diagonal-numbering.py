N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

num = 1
for i in range(N+M-1):
    for j in range(N):
        for k in range(M):
            if i == (j+k):
                arr[j][k] = num
                num += 1

for a in arr:
    print(*a)