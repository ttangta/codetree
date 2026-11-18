DR = [1, 0, -1, 0]
DC = [0, -1, 0, 1]

# K의 값을 기반으로 '방향' 정보를 가져오는 함수 -> 최초 K의 값으로 방향 찾기
def initial_dir(K):
    # K의 값에 따라 방향 결정
    for i in range(4):
        if K in directions[i]:
            return i

# K의 '방향'으로 '위치' 구하는 함수
def inital_position(K):
    # '위치' 구하는 함수 내에서 '방향' 정보 함수 호출
    dir_num = initial_dir(K)
    row = col = None
    # 행이 0으로 고정, 열의 값은 변경 (K -1)
    if dir_num == 0:
        row = 0
        col = K-1
    # 행의 값 변경(K%N), 열은 N-1로 고정
    elif dir_num == 1:
        row = (K-1) % N
        col = N - 1
    # 행이 N-1으로 고정, 열은 N*3 - K 값
    elif dir_num == 2:
        row = N - 1
        col = N*3 - K
    # 행이 N*4-K 값, 열은 0으로 고정
    elif dir_num == 3:
        row = N * 4 - K
        col = 0

    return dir_num, row, col

def in_range(row, col, N):
    return (row >= 0 and row < N) and (col >= 0 and col < N)

def solution(arr, N, K):
    # 최초 K의 값으로 초기 방향, 행, 열
    cur_dir, cur_row, cur_col = inital_position(K)

    answer = 0
    # 현재 위치가 배열 범위인 동안 반복
    while in_range(cur_row, cur_col, N):
        answer += 1
        nd = None
        # 들어오는 부분의 문자 확인
        c = arr[cur_row][cur_col]

        if c == '\\':
            nd = (4 - cur_dir - 1) % 4
        else:
            if cur_dir%2 == 0:
                nd = cur_dir+1
            else:
                nd = cur_dir-1
        cur_dir = nd
        cur_row += DR[cur_dir]
        cur_col += DC[cur_dir]
    return answer


N = int(input())
arr = [list(input()) for _ in range(N)]
K = int(input())
directions = []
for i in range(0, 4*N):
    if i % N == 0:
        directions.append([])
    directions[-1].append(i+1)
answer = solution(arr, N, K)
print(answer)
