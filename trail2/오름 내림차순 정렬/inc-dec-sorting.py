def solution(arr):
    arr.sort()
    print(*arr)
    print(*list(reversed(arr)))

n = int(input())
arr = list(map(int, input().split()))[:n]

solution(arr)