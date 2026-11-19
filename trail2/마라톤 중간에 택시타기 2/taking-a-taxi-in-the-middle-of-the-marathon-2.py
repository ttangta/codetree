import sys
def solution(N):
    answer = sys.maxsize

    # 첫번째, 마지막 요소 제외 중간에 건너뛰어볼 요소 범위
    # 매 반복에서 최초 이전 좌표 정보는 0번 인덱스로 고정
    for i in range(1, N-1):
        pre = 0
        total = abs(points[0][0] - points[0][0]) + abs(points[0][1] - points[0][1])
        # 0~(N-1) 까지 모든 요소에 접근하는 동안
        for j in range(N):
            # 제외하고자 하는 요소 인덱스와 접근한 인덱스의 번호가 같다면 건너뛰기
            if i == j: continue
            # j번째 요소가 건너뛸 요소가 아니라면 '이전 좌표'와 'j번 좌표' 를 가지고 택시 거리 계산 수행
            total += abs(points[pre][0] - points[j][0]) + abs(points[pre][1] - points[j][1])
            pre = j
        answer = min(answer, total)
    return answer

N = int(input())

points = []

for _ in range(N):
    x, y = map(int, input().split())
    x = int(x)
    y = int(y)
    points.append(tuple([x, y]))

print(solution(N))
