def solution(a, b):
    sum_val = cnt = 0

    for i in range(a, b+1):
        if i % 5 == 0 or i % 7 == 0:
            sum_val += i
            cnt += 1
    
    return sum_val, sum_val/cnt

a, b = map(int, input().split())

r1, r2 = solution(a, b)
print(f"{r1} {r2:.1f}")
