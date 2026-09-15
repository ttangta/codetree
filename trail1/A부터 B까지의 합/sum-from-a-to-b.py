def solution(a, b):
    sum_val = 0

    for i in range(a, b+1):
        sum_val += i

    return sum_val
a, b = map(int, input().split())

print(solution(a, b))