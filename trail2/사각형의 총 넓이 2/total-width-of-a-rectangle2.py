OFFSET = 101

arr = [[0] * (OFFSET*2) for _ in range((OFFSET*2))]

def mk_arr(x1, y1, x2, y2):
    global arr
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(y1, y2):
        for col in range(x1, x2):
            arr[row][col] = 1

def solution():
    cnt = 0
    for a in arr:
        cnt += a.count(1)
    return cnt


N = int(input())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    mk_arr(x1,y1,x2,y2)

answer = solution()
print(answer)