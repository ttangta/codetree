def solution(a, b):
    value = 1

    for i in range(1, b+1):
        if i % a == 0:
            value *= i

    return value

a, b = map(int, input().split())

print(solution(a, b))