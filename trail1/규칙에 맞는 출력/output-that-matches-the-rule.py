n = int(input())
num = n
for i in range(n):
    num = n-i
    for j in range(i+1):
        print(num, end= " ")
        num += 1
    print()