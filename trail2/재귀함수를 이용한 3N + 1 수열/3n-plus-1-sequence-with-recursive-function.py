def solution(level, N):
    if N == 1:
        return level

    if N % 2 == 0:
        N //= 2
        return solution(level+1, N)
    else:
        N = (N * 3) + 1
        return solution(level+1, N)

N = int(input())

print(solution(0, N))