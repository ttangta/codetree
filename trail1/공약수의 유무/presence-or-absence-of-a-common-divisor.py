def solution(a, b):
    for i in range(a, b+1):
        if 1920 % i == 0 and 2880 % i == 0:
            return 1

    return 0

a, b = map(int, input().split())
print(solution(a,b))
