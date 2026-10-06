n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    qu = list(map(int, input().split()))

    if qu[0] == 1:
        print(arr[qu[1]-1])
    elif qu[0] == 2:
        if qu[1] in arr:
            print(arr.index(qu[1])+1)
        else:
            print(0)
    elif qu[0] == 3:
        s, e = qu[1], qu[2]
        for i in range(s-1, e):
            print(arr[i], end = " ")
        print()
