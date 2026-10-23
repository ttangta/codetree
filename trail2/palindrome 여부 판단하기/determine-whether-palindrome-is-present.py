def solution(A):
    return A == A[::-1]

A = input()

if solution(A):
    print("Yes")
else:
    print("No")