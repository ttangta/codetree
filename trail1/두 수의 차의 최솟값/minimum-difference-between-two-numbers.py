import sys

N = int(input())

nums = list(map(int, input().split()))[:N]

answer = sys.maxsize

for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        gap = nums[i] - nums[j]
        answer = min(answer , gap)

print(answer)