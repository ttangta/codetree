def solution(N):
    if N <= 2:
        return N
    
    return solution(N-2) + N


N = int(input())
print(solution(N))