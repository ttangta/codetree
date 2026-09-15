def solution(arr):
    cnt_3 = cnt_5 = 0
    
    for a in arr:
        if a % 3 == 0: cnt_3 += 1
        if a % 5 == 0: cnt_5 += 1

    return cnt_3, cnt_5


arr = []
for i in range(10):
    arr.append(int(input()))

r1, r2 = solution(arr)
print(r1, r2)