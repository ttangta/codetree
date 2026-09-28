n = int(input())

c_num = ord('A')

for i in range(1, n+1):
    for j in range(i):
        if c_num > ord('Z'):
            c_num = ord('A')
        print(chr(c_num), end="")
        c_num += 1
    print()