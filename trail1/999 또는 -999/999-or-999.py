import sys

# 최대값 초기화
max_val = -sys.maxsize

# 최솟값 초기화
min_val = sys.maxsize

# 요소가 최대 100개인 배열생성 
nums = list(map(int, input().split()))[:100]

# 배열의 요소를 접근하다가 -999 또는 999값이 나타난 다면 해당 인덱스 이전의 배열만 사용하도록 슬라이싱
for i in range(len(nums)):
    if nums[i] == -999 or nums[i] == 999:
        nums = nums[:i]
        break

# 지정된 nums 배열 내에서 최대값과 최소값 갱신
for elem in nums:
    # 최대값 갱신
    if max_val < elem:
        max_val = elem

    # 최소값 갱신
    if min_val > elem:
        min_val = elem

print(max_val, min_val)