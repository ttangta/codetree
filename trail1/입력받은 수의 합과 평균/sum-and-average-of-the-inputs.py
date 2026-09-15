def solution(arr):
    cnt = len(arr)
    sum_val = 0

    for a in arr:
        sum_val += a
    
    return sum_val, sum_val / cnt

arr = []
n = int(input())

for i in range(n):
    arr.append(int(input()))

r1, r2 = solution(arr)
print(f"{r1} {r2:.1f}")