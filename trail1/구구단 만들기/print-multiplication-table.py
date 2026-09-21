a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1, 2):
    cnt += 1

for i in range(1, 10):
    t = 0
    for j in range(b, a-1, -1):
        if j % 2 == 0:
            t += 1   
            print(f"{j} * {i} = {j * i}", end="")
            if cnt > t:
                print(" / ", end ="")
    print()
