def solution(n):
    num = 2
    while num < n:
        if n % num == 0:
            return "C"
        num += 1

    return "N"
n = int(input())

print(solution(n))