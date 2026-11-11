OFFSET = 1000

arr = [[0] * ((OFFSET*2)+1) for _ in range((OFFSET * 2)+1)]

def mk_arr(info):
    x1,y1,x2,y2 = info[0], info[1], info[2], info[3]

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(y1, y2):
        for col in range(x1, x2):
            arr[row][col] = 1

def minus_arr(info):
    x1, y1, x2, y2 = info[0], info[1], info[2], info[3]

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(y1, y2):
        for col in range(x1, x2):
            arr[row][col] = 0


def solution():
    cnt = 0

    for a in arr:
        cnt += a.count(1)

    return cnt


A = list(map(int, input().split()))
mk_arr(A)
B = list(map(int, input().split()))
mk_arr(B)
M = list(map(int, input().split()))
minus_arr(M)
print(solution())