DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

def in_range(row, col, N):
    return (row >= 0 and row < N) and  (col >=0 and col < N)

def solution(arr, N):
    answer = 0

    for row in range(N):
        for col in range(N):
            cnt = 0
            for nr, nc in zip(DR, DC):
                next_row = row + nr
                next_col = col + nc
                if in_range(next_row, next_col, N) and arr[next_row][next_col] == 1:
                    cnt += 1
            if cnt >= 3:
                answer += 1

    return answer



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

print(solution(arr, N))