def solution(a, b):
    sum_val = 0

    if a > b:
        a, b = b, a

    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i

    return sum_val

a, b = map(int, input().split())
print(solution(a, b))
