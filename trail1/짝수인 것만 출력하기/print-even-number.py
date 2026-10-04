n = int(input())
arr = list(map(int, input().split()))

arr = [a for a in arr if a%2 == 0]

print(*arr)