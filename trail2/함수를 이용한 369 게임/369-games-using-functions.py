def solution(n):
    return n % 3 == 0 or is_inner(n)
    
def is_inner(n):
    n = str(n)
    return "3" in n or "6" in n or "9" in n

A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
    if solution(i):cnt +=1
print(cnt)