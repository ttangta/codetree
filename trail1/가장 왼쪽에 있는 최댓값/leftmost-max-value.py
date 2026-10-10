import sys

N = int(input())
nums = list(map(int, input().split()))[:N]

answer = []

# nums 배열의 요소가 1개 이상인 동안 반복
while len(nums) >= 1:
    # 매 반복에서 리스트 내 최대값을 찾기 위해 최대값 반복마다 초기환
    max_val = -sys.maxsize
    # nums 내 최대값일 경우의 인덱스 값을 나타내는 변수
    max_idx = None

    for i in range(len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i
    answer.append(max_idx +1)

    # nums 배열의 범위 조정
    nums = nums[:max_idx]

print(*answer)