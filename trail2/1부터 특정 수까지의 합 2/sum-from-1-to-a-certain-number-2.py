def recursion_solution(N):
    if N == 1:
        return 1

    return recursion_solution(N-1) + N
    
N = int(input())

print(recursion_solution(N))