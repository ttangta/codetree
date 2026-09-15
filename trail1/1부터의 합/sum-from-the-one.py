def solution(n):
    sum_val = 0
    result = 100
    for i in range(1, 100):
        sum_val += i

        if sum_val >= n:
            result = i
            break 
    return result
n = int(input())

print(solution(n))
