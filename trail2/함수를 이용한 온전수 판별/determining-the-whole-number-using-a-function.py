def condition1(n):
    return n % 2 != 0

def condition2(n):
    return n % 10 != 5

def condition3(n):
    return n % 3 != 0 or n % 9 == 0

def solution(n):
    return condition1(n) and condition2(n) and condition3(n)


A, B = map(int, input().split())

cnt = 0

for i in range(A, B+1):
    if solution(i): cnt +=1

print(cnt)
