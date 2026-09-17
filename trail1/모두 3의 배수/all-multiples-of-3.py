def solution(arr):
    for a in arr:
        if a % 3 != 0:
            return 0
    return 1
arr = []
for i in range(5):
    arr.append(int(input()))

print(solution(arr))