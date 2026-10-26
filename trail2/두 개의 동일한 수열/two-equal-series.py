def solution(A, B):
    A.sort()
    B.sort()
    return A == B

n = int(input())
A = list(map(int, input().split()))[:n]
B = list(map(int, input().split()))[:n]

if solution(A,B):
    print("Yes")
else:
    print("No")