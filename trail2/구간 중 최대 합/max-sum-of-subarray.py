import sys
def solution(N, K):
    # 최대값을 구하는 수 = 초기 정답을 시스템이 나타낼 수 있는 최소값으로 지정
    answer = -sys.maxsize

    for i in range(N-K+1):
        answer = max(answer, sum(nums[i:i+K]))

    return answer

N, K = map(int, input().split())

nums = list(map(int, input().split()))[:N]

print(solution(N, K))