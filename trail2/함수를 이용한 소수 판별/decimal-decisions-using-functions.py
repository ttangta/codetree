def solution(n):
    for i in range(2, n):
       if n % i == 0:return False
    return True 

A, B = map(int, input().split())
answer = 0
for i in range(A, B+1):
    if solution(i): answer += i
print(answer)