def solution(a, b):
    value = 1

    for i in range(b):
        value *= a

    return value
a, b = map(int, input().split())

print(solution(a,b))