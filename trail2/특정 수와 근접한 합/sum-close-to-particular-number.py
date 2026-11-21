import sys
def solution(N, M):
    # 문제에서는 배열 요소 개수 중 2개를 제외한 합이 S와 가장 근사한 값을 찾아야 하기 때문에 
    # 최초 S와의 값 차를 최대값으로 지정
    gap = sys.maxsize
    
    
    # 앞단 부터 total에서 nums[i] 값을 빼봄 -> 배열에서 1번째 요소를 빼는 상황
    for i in range(N-1):
        total = sum(nums)
        total -= nums[i]    
        for j in range(i+1,N):
            # i 이후의 요소를 하나 더 빼봄 -> 배열에서 2번째 요소를 빼는 상황
            total -= nums[j]

            # 현재 gap과 S - 2요소를 뺀 중 작은 값을 선택
            gap = min(gap, abs(total-S))
            total += nums[j]

    return gap
N, S = map(int, input().split())

nums = list(map(int, input().split()))

print(solution(N, S))