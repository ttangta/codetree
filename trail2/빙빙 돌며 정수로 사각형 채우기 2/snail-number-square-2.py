DR = [1, 0, -1, 0]
DC = [0, 1, 0, -1]

def is_valid(row, col, N, M):
    return (row >= 0 and row <N) and (col >= 0 and col < M)

def solution(N, M):
    dir_num = 0
    cur_row = cur_col = 0
    # 시작 위치의 값 초기화
    arr[cur_row][cur_col] = 1

    for i in range(2, N * M + 1):
        nr = cur_row + DR[dir_num]
        nc = cur_col + DC[dir_num]

        # nr, nc 가 범위 밖이거나 이미 값이 채워진 위치인 경우
        if not is_valid(nr, nc, N, M) or arr[nr][nc] != 0:
            dir_num = (dir_num + 1) % 4
            nr = cur_row + DR[dir_num]
            nc = cur_col + DC[dir_num]
        arr[nr][nc] = i
        cur_row = nr
        cur_col = nc

# N = 행, M = 열
N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

solution(N, M)

for a in arr:
    print(*a)
