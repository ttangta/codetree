def solution(arr):
    sum_val = 0

    for a in arr:
        if a % 2 != 0 and a % 3 == 0:
            sum_val += a

    return sum_val

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

print(solution(arr))