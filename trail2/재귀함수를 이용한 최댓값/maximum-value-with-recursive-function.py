def solution(level, N):
    if level == N:
        return 0

    return max(arr[level], solution(level+1, N))


N = int(input())
arr = list(map(int, input().split()))[:N]

print(solution(0, N))