def solution(n):
    sum_val = 0

    arr = [1]
    for i in range(2,(n//2)+1):
        if n % i == 0:
            arr.append(i)

    for a in arr:
        sum_val += a 
    
    if sum_val == n: return "P"
    else: return "N"

n = int(input())
print(solution(n))