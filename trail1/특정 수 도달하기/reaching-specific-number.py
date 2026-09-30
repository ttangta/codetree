arr = list(map(int, input().split()))

limit_idx = -1

for i in range(len(arr)):
    if arr[i] >= 250:
        limit_idx = i
        break

if limit_idx == -1:
    print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")

else:
    sum_v = 0
    cnt = 0
    for elem in arr[:limit_idx]:
        cnt += 1
        sum_v += elem
    print(f"{sum_v} {sum_v/cnt:.1f}")