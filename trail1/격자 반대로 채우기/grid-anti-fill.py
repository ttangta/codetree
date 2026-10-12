N = int(input())

arr = [[0] * N for _ in range(N)]

flag = True
num = 1
for i in range(N-1, -1, -1):
    if flag:
        for j in range(N-1, -1, -1):
            arr[j][i] = num
            num += 1
        flag = False
    else:
        for j in range(N):
            arr[j][i] = num
            num += 1
        flag = True
for a in arr:
    print(*a)