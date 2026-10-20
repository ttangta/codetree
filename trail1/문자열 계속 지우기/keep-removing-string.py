A = input()
B = input()

start = A.find(B)

while start != -1:
    A = A[:start] + A[(start+len(B)):]

    start = A.find(B)

print(A)