A = input()
cmd = input()

for c in cmd:
    if c == "L":
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[0:-1]

print(A)