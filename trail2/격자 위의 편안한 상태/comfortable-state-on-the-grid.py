DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

# N : 격자 크기, M : 명령어 갯수
N, M = map(int, input().split())

arr = [[0] * N for _ in range(N)]


def in_range(row, col, N):
    return (row >= 0 and row < N) and (col >= 0 and col < N)

def solution(cmd, N):
    # 각 명령어의 위치에 색칠 후 해당 칸의 상태 정보를 누적할 정답 배열
    answer = []

    # 각 색칠될 명령어 수행
    for row, col in cmd:
        row = row - 1
        col = col - 1
        # 현재 명령어 위치를 색칠
        arr[row][col] = 1

        # 색칠한 뒤 인접한 칸에 색칠된 칸이 3개인지 확인
        cnt = 0
        for i in range(4):
            nr = row + DR[i]
            nc = col + DC[i]
            if in_range(nr, nc, N):
                if arr[nr][nc] == 1:
                    cnt+=1

        if cnt == 3:
            answer.append(1)
        else:
            answer.append(0)

    return answer


cmd = []
for _ in range(M):
    cmd.append(tuple(map(int, input().split())))

answer = solution(cmd, N)

for a in answer:
    print(a)