def solution(A):
    answer = 0
    n = len(A)
    for i in range(n-1):
        if A[i] == ')':
            continue
        for j in range(i+1, n):
            if A[j] == ')':answer += 1
    return answer
A = input()

print(solution(A))