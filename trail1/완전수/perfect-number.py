start, end = map(int, input().split())

cnt = 0

for i in range(start, end+1):
    # i의 진약수를 담을 배열
    arr = []
    for j in range(1,i):
        if i%j== 0: arr.append(j)

    check = sum(arr)

    if check == i:
        cnt += 1

print(cnt)