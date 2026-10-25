def solution(N):
    if N == 1 or N == 2:
        return 1

    return solution(N-2) + solution(N-1)

N = int(input())

print(solution(N))