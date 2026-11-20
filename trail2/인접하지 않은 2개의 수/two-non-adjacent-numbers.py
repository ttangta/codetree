import sys
def solution(N):
    # 최대값을 구하는 문제이므로 최촉값은 시스템이 표현하는 가장 작은 값으로 지정
    # 반드시 최소 한 번의 갱신은 일어날 수 있도록
    answer = -sys.maxsize

    # 인접한 두 수가 선택되지 않을 때 i이후 접근할 인덱스 번호가 i+2의 값이 될 수 있도록
    # 범위 조정
    for i in range(N-2):
        sum = nums[i]
        # 현재 i의 인덱스 위치에서 2칸 떨어져 있는 인덱스 부터 마지막 인덱스 값까지 도착하기 위한 범위 조정
        for j in range(i+2, N):
            # 선택되어 있는 i번째 인덱스 값에 j인덱스 값 더해봄 -> 현재 정답값과 sum의 값을 비교해 큰 값으로 갱신
            sum += nums[j]
            answer = max(answer, sum)

            # 정답값 갱신 후 sum에 j의 값이 누적하여 더해지는 것을 방지하기 위해 현재 j 인덱스 값을 빼주기
            sum -= nums[j]

    return answer

N = int(input())

nums = list(map(int, input().split()))[:N]

print(solution(N))
