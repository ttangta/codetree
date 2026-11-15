# 상하좌우에 현재 위치에서 이동해야 할 값
DP = [(-1,0), (1,0), (0, -1), (0, 1)]

# 이동해야하는 방향 D에 따른 DP의 인덱스를 값으로 가지는 디렉토리
DI = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}

# 배열 내 유효한 범위인지 판단하는 함수
def in_range(row, col, N):
    return (row >=0 and row < N) and (col >=0 and col < N)


def solution(arr, T, R, C, D):
    cur_row = R
    cur_col = C
    cur_d = DI.get(D)
    for _ in range(T):
        nr = cur_row + DP[cur_d][0]
        nc = cur_col + DP[cur_d][1]

        # 지정된 방향으로 이동 가능한 경우
        if in_range(nr, nc, N):
            # 공을 나타내는 1의 값을 현재 위치는 0으로 변경 
            arr[cur_row][cur_col] = 0
            # 다음 위치의 값을 1로 변경하여 공이 다음 위치로 이동되었음을 나타냄
            arr[nr][nc] = 1

            # 현재 위치 갱신
            cur_row = nr
            cur_col = nc
        # 지정된 방향으로 이동이 불가능한 경우 -> 이동 방향만 반대로 변경
        else:
            if cur_d % 2 == 0:
                cur_d += 1
            else:
                cur_d -= 1
    answer = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                answer = tuple([(i+1), (j+1)])
                break
    return answer    

N, T = map(int, input().split())

arr = [[0] * N for _ in range(N)]

R, C, D = input().split()

R = int(R)-1
C = int(C)-1

arr[R][C] = 1

a1, a2 = solution(arr, T, R, C, D)
print(a1, a2)