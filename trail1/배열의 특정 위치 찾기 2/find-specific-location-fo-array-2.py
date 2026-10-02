arr = list(map(int, input().split()))

sum_1 = sum(arr[::2])
sum_2 = sum(arr[1::2])

max_v = max(sum_1, sum_2)
min_v = min(sum_1, sum_2)

print(max_v - min_v)