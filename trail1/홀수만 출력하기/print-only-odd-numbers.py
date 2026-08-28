N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
for i in nums:
    if i%2 == 1 and i%3==0:
        print(i)