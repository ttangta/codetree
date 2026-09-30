n = int(input())

for i in range(2, n+1):
    is_true = True
    for j in range(2, i):
        if i % j == 0:
            is_true = False
            break
    if is_true:
        print(i, end = " ")
    