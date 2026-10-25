def solution(N):
    if N < 10:
        return N

    return solution(N//10) + N%10

a, b, c = map(int, input().split())

N = a * b * c

print(solution(N))