import sys

# 최소값 초기화
min_val = sys.maxsize

min_cnt = 0

N = int(input())

nums = list(map(int, input().split()))


for elem in nums:
    # 현재 최소값 보다 elem 값이 크가면 min_val 갱신
    if min_val > elem:
        min_val = elem

for elem in nums:
    if min_val == elem:min_cnt+=1

print(min_val, min_cnt)