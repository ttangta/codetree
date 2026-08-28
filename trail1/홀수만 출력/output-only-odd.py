str = input()
A = int(str.split()[0])
B = int(str.split()[1])

for i in range(A, B+1):
    if i%2 == 1:
        print(i, end=' ')