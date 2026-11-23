import sys
def solution(N, H, T):
    # 최소값을 구해야 하므로 초기 정답은 시스템이 나타낼 수 있는 값 지정
    answer = sys.maxsize

    # 연속 구간이 T가 될 수 있도록 탐색 범위 지정
    for i in range((N-T)+1):
        part = arr[i: (i+T)]
        sum = 0
        for p in part:
            sum += abs(H - p)
        answer = min(answer, sum)

    return answer

N, H, T = map(int, input().split())

arr = list(map(int, input().split()))[:N]

answer = solution(N, H, T)

print(answer)