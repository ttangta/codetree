def r1(N):
    if N == 0:
        return 

    r1(N-1)
    print(N, end = " ")

def r2(N):
    if N == 0:
        return 

    print(N, end = " ")
    r2(N-1)

def solution(N):
    r1(N)

    print()

    r2(N)

    print()

N = int(input())

solution(N)