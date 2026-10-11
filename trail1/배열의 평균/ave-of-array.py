arr = [list(map(int, input().split()))[:4] for _ in range(2)]

# print(arr)
total_sum =  0


for i in range(2):
    row_sum = 0
    for j in range(4):
        total_sum += arr[i][j]
        row_sum += arr[i][j]
    print(f"{(row_sum/4):.1f}", end = " ")   
print()
for j in range(4):
    col_sum = 0
    for i in range(2):
        col_sum += arr[i][j]
    print(f"{(col_sum/2):.1f}", end = " ")
print()
print(f"{(total_sum)/(4*2):.1f}")
