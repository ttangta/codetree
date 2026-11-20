DR = [-1, 1, 0, 0, -1, -1, 1, 1]
DC = [0, 0, -1, 1, -1, 1, -1, 1]

def in_range(row, col, N, M):
    return row >= 0 and row < N and col >= 0 and col < M

def solution(N, M):
    answer = 0

    for row in range(N):
        for col in range(M):
            cur = arr[row][col]

            # 만약 현재 위치의 값이 'L' 이면 각 방향으로 두 칸 씩 이동해보며 이동한 칸이 모두 'E' 인지 확인
            if cur == 'L':
                for i in range(8):
                    flag = True
                    for j in range(1, 3):
                        nr = row + DR[i] * j
                        nc = col + DC[i] * j

                        if not in_range(nr, nc, N, M) or arr[nr][nc] != 'E':
                            flag = False
                            break

                    if flag: answer += 1

    return answer


N, M = map(int, input().split())

arr = [list(input())[:M] for _ in range(N)]

print(solution(N, M))
