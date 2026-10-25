def solution(N):
    if N <= 2:
        return N

    return solution(N//3) + solution(N-1)

N = int(input())
print(solution(N))