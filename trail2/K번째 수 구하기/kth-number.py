def solution(arr, k):
    arr.sort()
    return arr[k-1]

n, k = map(int, input().split())
arr = list(map(int, input().split()))[:n]

print(solution(arr, k))