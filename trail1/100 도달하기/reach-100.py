n = int(input())
arr = []
arr.append(1)
arr.append(n)

pp = 0
p = 1

while True:
    num = arr[pp] + arr[p]
    arr.append(num)

    pp += 1
    p += 1

    if num >= 100:
        break

print(*arr)