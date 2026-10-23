DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(M, D):
    return  1 <= M <= 12 and(1 <= D <= DAYS[M])
    M, D = map(int, input().split())


M, D = map(int, input().split())
if solution(M, D):
    print("Yes")
else:
    print("No")