N = int(input())

arr = []


sum_v = cnt = 0
for _ in range(N):
    arr.append(input())

c = input()


for a in arr:
    if a[0] == c:
        sum_v += len(a)
        cnt += 1

print(f"{cnt} {sum_v/cnt:.2f}")