n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        num = i+j
        print(f"({i}, {j})", end= " ")
        if num%4 == 0:
            print()
print()