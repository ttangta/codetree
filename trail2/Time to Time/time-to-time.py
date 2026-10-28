def solution(A, B, C, D):
    start = (A*60) + B
    end = (C*60) + D

    return end - start


A, B, C, D = map(int, input().split())
answer = solution(A,B,C,D)
print(answer)