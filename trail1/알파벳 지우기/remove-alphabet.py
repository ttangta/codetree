A = input()
B = input()

arr_a = []
arr_b = []

for i in range(len(A)):
    if A[i].isnumeric():
        arr_a.append(A[i])

for i in range(len(B)):
    if B[i].isnumeric():
        arr_b.append(B[i])

A = int("".join(arr_a))
B = int("".join(arr_b))

print(A+B)