n = int(input())
n2 = n
for i in range(1, n+1):
    for j in range(1, n2+1):
        if j == n2:
            print(f"{i} * {j} = {i*j}")
        else:
            print(f"{i} * {j} = {i*j}", end=" / ")
    n2 -= 1