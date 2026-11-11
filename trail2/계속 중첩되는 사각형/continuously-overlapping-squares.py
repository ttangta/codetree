OFFSET = 100
arr_len = OFFSET * 2 + 1

arr = [[0] * arr_len for _ in range(arr_len)]

def mk_arr(round, info):
    val = ''
    # i번째 순서가 짝수 번째 순서면 빨강색으로 칠하기
    if round % 2 == 0:
        val = 'r'
    # i번째 순서가 홀수 번째 순서라면 파랑색으로 칠하기
    else:
        val = 'b'

    x1, y1, x2, y2 = info[0], info[1], info[2], info[3]
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(y1, y2):
        for col in range(x1, x2):arr[row][col] = val


def solution():
    cnt = 0
    for a in arr:
        cnt += a.count('b')

    return cnt

N = int(input())

for i in range(N):
    info = list(map(int, input().split()))
    mk_arr(i, info)

answer = solution()
print(answer)