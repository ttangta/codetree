def solution(n,arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //=2

n = int(input())

arr = list(map(int, input().split()))[:n]

solution(n,arr)

print(*arr)
