def solution(n, m):
    if n < m:
        n, m = m, n
    answer = float("-inf")
    
    for i in range(1, m+1):
        if n % i == 0 and m % i == 0:
            answer = max(answer, i)
    return answer

n, m = map(int, input().split())

answer = solution(n, m)

print(answer)