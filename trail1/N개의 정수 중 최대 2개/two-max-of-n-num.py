N = int(input())

nums = list(map(int, input().split()))[:N]

for i in range(N-1):
    for j in range(N-1, i, -1):
        if nums[j] > nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]

print(nums[0], nums[1])