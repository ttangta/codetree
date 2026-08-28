A, B = map(int, input().split())
if A > B:
    temp = A
    A = B
    B = temp
for i in range(B, A-1, -1):
    print(i, end=' ')