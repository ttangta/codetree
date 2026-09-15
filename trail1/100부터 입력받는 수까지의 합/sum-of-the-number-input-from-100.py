def solution(n):
    sum_val = 0

    for i in range(n, 101):
        sum_val += i

    return sum_val

n = int(input())

print(solution(n))