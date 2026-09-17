def solution(n):
    for i in range(2, n):
        if n % i == 0:
            return "C"
    return "P"
n = int(input())
print(solution(n))