def recursion_solution(N):
    if N == 0:
        return 

    recursion_solution(N-1)

    print("*" * N)

N = int(input())

recursion_solution(N)