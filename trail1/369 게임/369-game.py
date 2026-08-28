N = int(input())

for i in range(1, N+1):
    s_n = str(i)
    flag = False
    for s in s_n:
        if s == '3' or s == '6' or s == '9':
            flag = True
            break
    if i%3 == 0 or flag:
        print(0, end=' ')
    else:
        print(i, end=' ')

