def solution(N):
    if N <= 2:
        return N * 2

    return (solution(N-2) * solution(N-1)) % 100
N = int(input())

print(solution(N))