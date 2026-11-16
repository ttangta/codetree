# 현재 행, 열에서 다음 번 위치로 이동하기 위해 현재 위치에 더해야할 값
# 순서 : 오른쪽 -> 아래 -> 왼쪽 -> 위쪽
DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

# 입력받은 행과 열의 값이 범위 내에 유효한 값인지 판단하는 함수
# -> 격자 내에서 이동가능한 방향인지 판단하는 역할로 사용
def is_range(row, col, N, M):
    return (row >= 0 and row < N) and (col >= 0 and col < M)

# 달팽이 모양으로 값을 채우는 함수
def solution(arr, N, M):
    # N * M 배열의 모든 위치에 값을 채울 때
    # 현재 위치를 가리키는 좌표
    # 최초 함수 호출 시 (0, 0) 으로 초기화
    cur_r = cur_c = 0

    # 현재 이동하는 방향을 나타내는 변수
    dir = 0

    # 최초 (0, 0) 좌표의 값은 1
    arr[cur_r][cur_c] = 1

    # (0, 0) 좌표에 1을 채운 이후부터 N * M 까지 값을 채우기 위한 반복 시작
    for i in range(2, N*M+1):
        # 현재 행에서 이동해야할 다음 행 번호
        nr = cur_r + DR[dir]
        nc = cur_c + DC[dir]

        # 현재 위치에서 이동하고자 하는 방향이 접근 불가능한 조건인 경우 -> 이동하는 방향을 나타내는 값 변경
        # 배열 범위 바깥이거나 이미 해당 위치에 값이 지정되어 있는 경우 방향 번호 변경
        if not is_range(nr, nc, N, M) or arr[nr][nc] != 0:
            dir = (dir+1)%4
        
        # 이동 방향 번호가 변경된 경우를 생각해 다음 행, 다음 열의 값을 갱신
        nr = cur_r + DR[dir]
        nc = cur_c + DC[dir]
        arr[nr][nc] = i

        # 다음 행을 채운 이후 현재행을 다음행으로 갱신
        cur_r = nr
        cur_c = nc

# N = 행
# M = 열
N, M = map(int, input().split())

# 모든 값이 0으로 초기화된 N * M 크기의 배열 생성
arr = [[0] * M for _ in range(N)]

solution(arr, N, M)

for a in arr:
    print(*a)