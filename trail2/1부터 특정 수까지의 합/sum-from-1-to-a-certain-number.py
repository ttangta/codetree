def solution(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    
    return sum_v // 10

answer = solution(int(input()))
print(answer)