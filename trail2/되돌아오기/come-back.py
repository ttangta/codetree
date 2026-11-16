# 명령어의 최대 개수는 100개 한 번의 명령어에서 이동할 수 있는 최대 거리는 10
# 한쪽을 편향된 이동은 100 * 10 = 1000 이를 양쪽 이동으로 생각 = 2000, 그리고 중앙값을 초기화 하기위해 +1
OFFSET = (100 * 10)*2+ 1

arr = [[0] * OFFSET for _ in range(OFFSET)]

# '상 -> 하 -> 좌 -> 우' 인덱스 OFFSET 지정
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]
# 생성된 배열의 정중앙 위치에 값을 1로 초기화
arr[OFFSET//2][OFFSET//2] = 1

def in_range(row, col):
    return (row >= 0 and row < OFFSET) and (col >= 0 and col < OFFSET)
def solution(cmd):
    time = 1

    # 현재 행과 열, 최초 위치는 현재 1이 있는 위치 OFFSET // 2
    cur_r = cur_c = OFFSET // 2
    for d, l in cmd:
        dir = None
        if d == 'N':
            dir = 0
        elif d == 'S':
            dir = 1
        elif d == 'W':
            dir = 2
        elif d == 'E':
            dir = 3

        for i in range(l):
            nr = cur_r + DR[dir]
            nc = cur_c + DC[dir]

            # l초 동안 지정된 방향으로 이동
            if in_range(nr, nc):
                # 이동 중 만약 이동된 위치의 값이 1이라면 바로 함수 종료
                if arr[nr][nc] == 1:return time
                arr[cur_r][cur_c] = time
                time += 1

                # 위치 이동후 현재 위치를 이동된 위치로 변경
                cur_r = nr
                cur_c = nc

    # 모든 명령어를 이동하는 동안 1에 도착하지 못한다면 -1 반환
    return -1


N = int(input())

cmd = []
for _ in range(N):
    d, l = input().split()
    l = int(l)
    cmd.append(tuple([d, l]))


answer = solution(cmd)

print(answer)