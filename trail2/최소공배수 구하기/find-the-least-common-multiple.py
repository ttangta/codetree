def solution(n, m):
    if n > m:
        n, m = m, n
    mul_n = n
    mul_m = m
    cnt_n = cnt_m = 2
    answer = float("inf")
    while True:
        if mul_n == mul_m:
            answer = min(answer, mul_n)
            break
        if mul_n < mul_m:
            mul_n = n * cnt_n
            cnt_n += 1
        else:
            mul_m = m * cnt_m
            cnt_m += 1
            
    return answer
n, m = map(int, input().split())

answer = solution(n, m)
print(answer)