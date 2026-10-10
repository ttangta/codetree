import sys

max_val = -sys.maxsize

nums = list(map(int, input().split()))

for value in nums:
    if max_val < value:
        max_val = value

print(max_val)
