# 정해져있는 가로, 세로 길이
LEN = 8

# 최저 음수 좌표를 양수화 하기 위한 최소값
OFFSET = 100

def mk_arr(x, y):
    for row in range(y, y+8):
        for col in range(x, x+8):
            arr[row][col] = 1

def solution():
    cnt = 0
    for a in arr:
        cnt += a.count(1)

    return cnt


arr = [[0] * ((OFFSET * 2)+1) for _ in range(((OFFSET * 2) + 1))]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    mk_arr(x, y)

answer = solution()
print(answer)
