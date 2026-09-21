n = int(input())

cnt = 1

for i in range(n):
    for j in range(n):
        if cnt % 10 == 0:
            cnt += 1
        print(cnt % 10, end = "")
        cnt += 1
    print()