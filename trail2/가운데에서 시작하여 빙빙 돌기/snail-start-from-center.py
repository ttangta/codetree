DR = [0, -1, 0, 1]
DC = [-1, 0, 1, 0]

def in_range(row, col, N):
    return (row >= 0 and row < N) and (col >= 0 and col < N)

def solution(N):
    dir_num = 0
    cur_r = cur_c = N-1
    for i in range(N*N, 0, -1):
        arr[cur_r][cur_c] = i
        nr = cur_r + DR[dir_num]
        nc = cur_c + DC[dir_num]

        if not in_range(nr, nc, N) or arr[nr][nc] != 0:
            dir_num = (dir_num+1) % 4

        cur_r += DR[dir_num]
        cur_c += DC[dir_num]

N = int(input())
arr = [[0] * N for _ in range(N)]

solution(N)

for a in arr:
    print(*a)