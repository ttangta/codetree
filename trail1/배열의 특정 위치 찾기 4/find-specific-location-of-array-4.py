arr = list(map(int, input().split()))

for i in range(10):
    if arr[i] == 0:
        arr = arr[:i]
        break

cnt = 0
sum_v = 0

for a in arr:
    if a % 2 == 0:
        cnt += 1
        sum_v += a

print(f"{cnt} {sum_v}")