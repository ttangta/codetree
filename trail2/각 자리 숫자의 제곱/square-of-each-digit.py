def recursion_solution(N):
    if N < 10:
        return N ** 2

    return recursion_solution(N//10) + (N % 10) ** 2

N = int(input())

print(recursion_solution(N))