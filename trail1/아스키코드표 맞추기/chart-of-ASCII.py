arr = list(map(int, input().split()))[:5]

for i in range(5):
    arr[i] = chr(arr[i])

print(*arr)