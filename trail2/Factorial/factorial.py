def solution(N):
    if N <= 1:
        return 1

    return solution(N-1) * N

N = int(input())

print(solution(N))