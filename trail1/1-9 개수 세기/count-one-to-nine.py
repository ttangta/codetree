arr_cnt = [0] * 10
n = int(input())

arr = list(map(int, input().split()))[:n]

for a in arr:
    arr_cnt[a] += 1

for i in range(1, 10):
    print(arr_cnt[i])