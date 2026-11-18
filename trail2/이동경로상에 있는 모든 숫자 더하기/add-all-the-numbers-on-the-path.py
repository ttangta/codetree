DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def in_range(row, col, N):
    return (row >= 0 and row < N) and (col >= 0 and col < N)

def solution(N, T, cmd, arr):
    cur_r = cur_c = N // 2
    dir_num = 0
    answer = arr[cur_r][cur_c]

    for c in cmd:
        if c == 'R':
            dir_num = (dir_num+ 1) % 4
        elif c == 'L':
            dir_num = (dir_num + 4 - 1) % 4
        elif c == 'F':
            nr = cur_r + DR[dir_num]
            nc = cur_c + DC[dir_num]

            if in_range(nr, nc, N):
                answer += arr[nr][nc]
                cur_r = nr
                cur_c = nc

    return answer



N, T = map(int, input().split())

cmd = list(input())[:T]
arr = []
for i in range(N):
    arr.append([])
    arr[-1] = list(map(int, input().split()))

answer = solution(N, T, cmd, arr)

print(answer)