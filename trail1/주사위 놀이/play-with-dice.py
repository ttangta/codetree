arr_cnt = [0] * 7
arr = list(map(int, input().split()))[:10]

for a in arr:
    arr_cnt[a] += 1

for i in range(1, 7):
    print(f"{i} - {arr_cnt[i]}")