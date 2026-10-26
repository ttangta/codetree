def solution(arr):
    arr.sort()


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

solution(arr)

for a in arr:
    print(a)