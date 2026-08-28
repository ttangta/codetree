C, A = input().split()
A = int(A)
if C == 'A':
    for i in range(1,A+1):
        print(i, end=' ')
else:
    for i in range(A, 0, -1):
        print(i, end=' ')