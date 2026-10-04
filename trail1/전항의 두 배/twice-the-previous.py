n, m = map(int, input().split())

arr = [0] * 10
arr[0] = n
arr[1] = m
for i in range(2, 10):
    arr[i] = arr[i-1] + (2 * arr[i-2])

print(*arr)