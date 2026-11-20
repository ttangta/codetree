import sys
def solution(N):
    # 최소값을 찾는 문제이기 때문에 초기값을 가장 큰 값으로 잡아 한 번이상 무조건 갱신 될 수 있도록 설정
    answer = sys.maxsize

    # 각 방을 시작 지점이라고 했을 때
    for i in range(N):
        # 시작 방기준 j방 까지의 거리를 구하고 인원수 만큼 곱하여 누적
        sum = 0
        for j in range(N):
            gap = (N-i+j)%N
            sum += (rooms[j] * gap)
        # i방이 시작점 일때 모든 방에 인원이 배치되었을 경우 이동거리와 현재 정답 중 작은 값을 비교하여 정답 갱신
        answer = min(answer, sum)
    return answer


N = int(input())

rooms = []

for _ in range(N):
    rooms.append(int(input()))

print(solution(N))