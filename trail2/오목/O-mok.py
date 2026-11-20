#현재 위치 기준 - (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하) 이동에 필요한 값 배열 생성
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# 이동된 x,y 값이 지정된 배열 범위 내의 값인지 확인 함수
def in_range(row, col):
    return row >= 0 and row < 19 and col >= 0 and col < 19

def solution():
    for i in range(19):
        for j in range(19):
            cur = arr[i][j]
            # cur값이 1 또는 2 인 경우 로직 실행
            if cur:
                # 각 방향에서 매번 조건을 모두 부합하는지 확인 -> 방향이 변경될 때마다 승리 판단 True로 갱신
                for k in range(len(DELTA)):
                    winner = True
                    last_row = i
                    last_col = j
                    for z in range(1, 5):
                        nr = i + (DELTA[k][0]*z)
                        nc = j + (DELTA[k][1]*z)
                        last_row = nr
                        last_col = nc
                        # 현재에서 z번째 이동한 좌표의 값이 배열 밖이거나 이동된 값이 cur과 같은 값이 아니라면 승리조건에 부합하지 못함
                        if not in_range(nr, nc) or cur != arr[nr][nc]:
                            winner = False
                            break
                    if winner: return i, j, last_row, last_col

    return 0

arr = [list(map(int, input().split()))[:19] for _ in range(19)]

answer = solution() if solution() != 0 else 0

if answer != 0:
    answer_r, answer_c = (answer[0] + answer[2])//2, (answer[1] + answer[3])//2
    print(arr[answer_r][answer_c])
    print(answer_r+1, answer_c+1)
else:
    print(answer)