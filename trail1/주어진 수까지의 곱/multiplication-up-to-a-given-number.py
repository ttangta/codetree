def solution(a, b):
    value = 1

    for i in range(a, b+1):
        value *= i

    return value

a, b = map(int, input().split())

print(solution(a,b))