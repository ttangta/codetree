def recursion_solution(N, cnt):
    if N == 1:
        return cnt

    if N % 2 == 0:
        return recursion_solution(N//2, cnt+1)
    else:
        return recursion_solution(N//3, cnt+1)

N = int(input())

print(recursion_solution(N, 0))