def solution(n1, n2, A, B):
    for i in range(n1-n2+1):
        start = i
        end = i + n2
        if A[start:end] == B: return True
    return False


n1, n2 = map(int, input().split())

A = list(map(int, input().split()))[:n1]
B = list(map(int, input().split()))[:n2]


if solution(n1, n2, A, B):
    print("Yes")
else:
    print("No")