arr = [list(map(int, input().split()))[:4] for _ in range(4)]
sum_val = 0
for i in range(4):
    for j in range(0, i+1):
        sum_val += arr[i][j]

print(sum_val)