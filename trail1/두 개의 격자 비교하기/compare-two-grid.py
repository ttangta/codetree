N, M = map(int, input().split())

arr1 = [list(map(int, input().split()))[:M] for _ in range(N)]
arr2 = [list(map(int, input().split()))[:M] for _ in range(N)]

result = []

for i in range(N):
    arr = []
    for j in range(M):
        if arr1[i][j] == arr2[i][j]: arr.append(0)
        else: arr.append(1)
    result.append(arr)


for r in result:
    print(*r)