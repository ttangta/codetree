n = int(input())

arr = [0] * 11

arr[0] = n



for i in range(1, 11):
    arr[i] = arr[0] * i

cnt = 0
for i in range(1, 11):
    print(arr[i], end = " ")
    if arr[i] % 5 == 0:
        cnt += 1
    if cnt >= 2:
        break