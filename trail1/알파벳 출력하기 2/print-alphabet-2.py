n = int(input())

num = ord('A')
for i in range(n, -1, -1):
    for j in range((n-i)):
        print("  ", end ="")
    for j in range(i):
        if num > ord('Z'):
            num = ord('A')
        print(chr(num), end = " ")
        num += 1
    print()