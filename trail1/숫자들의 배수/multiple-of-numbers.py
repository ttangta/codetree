n = int(input())

arr = [0] * 11

arr[0] = n

cnt = 0

stop_idx = -1
for i in range(1, 11):
    arr[i] = arr[0] * i
    if arr[i]%5 == 0:
        cnt += 1
    if cnt == 2:
        stop_idx = i
        break

if stop_idx != -1:
    print(*arr[1:stop_idx+1])
else:
    print(*arr)
