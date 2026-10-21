A, B = input().split()

a_end = None
b_end = None

for i in range(len(A)):
    if not A[i].isnumeric():
        a_end = i
        break

for i in range(len(B)):
    if not B[i].isnumeric():
        b_end = i
        break
A = A[:a_end]
B = B[:b_end]

print(int(A) + int(B))    