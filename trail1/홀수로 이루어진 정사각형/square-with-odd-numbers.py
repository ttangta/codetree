n = int(input())

num = 11

for i in range(n):
    s = num
    for j in range(n):
        print(s, end = " ")
        s += 2
    
    num += 2
    print()