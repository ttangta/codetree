arr = [input().split()[:3] for _ in range(5)]

# print(arr)

for i in range(5):
    for j in range(3):
        arr[i][j] = chr(ord(arr[i][j]) - 32)

for i in range(5):
    print(*arr[i])