def solution(n):
    value = 1
    result = 0
    for i in range(1, 11):
        value *= i
        if value >= n:
            result = i
            break
        

    return result
n = int(input())

print(solution(n))