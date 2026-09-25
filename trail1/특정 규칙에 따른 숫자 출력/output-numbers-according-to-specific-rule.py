n = int(input())
num = 1
for i in range(n, 0, -1):
    print("  " * (n-i), end= "")
    for j in range(i, 0, -1):
        print(num, end=" ")
        num += 1
        if num == 10:
            num %= 9
    print()