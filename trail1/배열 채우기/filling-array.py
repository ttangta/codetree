arr = list(map(int, input().split()))

limit_idx = -1

for i in range(len(arr)):
    if arr[i] == 0:
        limit_idx = i

if limit_idx == -1:
    print(*arr[::-1])
else:
    arr = arr[:limit_idx]
    print(*arr[::-1])