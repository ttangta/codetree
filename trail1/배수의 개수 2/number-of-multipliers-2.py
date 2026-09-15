def solution(arr):
    cnt = 0

    for a in arr:
        if a % 2 != 0: cnt +=1 

    return cnt
arr = []

for i in range(10):
    arr.append(int(input()))

print(solution(arr))

