def solution(arr):
    sum_val = cnt = 0

    for a in arr:
        if 0<=a<=200:
            sum_val += a
            cnt += 1
    
    return sum_val, sum_val/cnt


arr = []

for i in range(10):
    arr.append(int(input()))

r1, r2 = solution(arr)
print(f"{r1} {r2:.1f}")