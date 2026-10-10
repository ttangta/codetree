STANDARD = 500

# 각각 500 미만, 초과의 값을 담을 배열 생성
under = []
over = []

nums = list(map(int, input().split()))[:10]

for elem in nums:
    if elem < STANDARD:
        under.append(elem)
    if elem > STANDARD:
        over.append(elem)

import sys

max_val = -sys.maxsize
min_val = sys.maxsize

for elem in under:
    if max_val < elem:
        max_val = elem

for elem in over:
    if min_val > elem:
        min_val = elem

print(max_val, min_val)