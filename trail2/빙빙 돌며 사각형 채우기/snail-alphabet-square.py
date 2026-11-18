DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

def in_range(row, col, N, M):
    return (row >= 0 and row < N) and (col >= 0 and col < M)

def solution(N, M):
    dir_num = 0
    cur_r = cur_c = 0
    for i in range(0, N*M):
        arr[cur_r][cur_c] = chr((i % 26)+65)
        nr = cur_r + DR[dir_num]
        nc = cur_c + DC[dir_num]

        if not in_range(nr, nc, N, M) or arr[nr][nc] != 0:
            dir_num = (dir_num+1) % 4

        cur_r += DR[dir_num]
        cur_c += DC[dir_num]

N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

solution(N, M)

for a in arr:
    print(*a)