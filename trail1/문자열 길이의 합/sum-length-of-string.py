N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

sum_v = cnt_a = 0
for a in arr:
    sum_v += len(a)
    if a.find("a") == 0:
        cnt_a += 1
print(sum_v, cnt_a)