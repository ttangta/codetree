def recursion_solution(N):
    if N == 0:
        return 

    print(N, end = " ")
    recursion_solution(N-1)
    print(N, end = " ")


N = int(input())

recursion_solution(N)

print()