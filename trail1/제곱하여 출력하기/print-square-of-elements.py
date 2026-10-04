n = int(input())
arr = list(map(int, input().split()))[:n]

arr = [a ** 2 for a in arr]
print(*arr)