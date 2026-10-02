arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

answer = arr[-1] + arr[-2] + arr[-3]
print(answer)