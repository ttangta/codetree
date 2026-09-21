n = int(input())

even = 1
odd = n

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            if even > n:
                even = 1
            print(even,end="")
        else:
            if odd < 1:
                odd = n
            print(odd, end="")
    even += 1
    odd -= 1
    print()