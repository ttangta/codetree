n = int(input())


for i in range(n):
    row = i + 1
    s = n * row
    for j in range(n):
        print(s, end = " ")
        s -= row
    print()