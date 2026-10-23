def solution(n, arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] *= -1

n = int(input())

arr = list(map(int, input().split()))[:n]

solution(n, arr)
print(*arr)