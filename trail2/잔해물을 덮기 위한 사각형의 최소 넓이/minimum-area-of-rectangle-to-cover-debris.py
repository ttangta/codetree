def solution():
    # 1이 존재하는 양단의 행의 값 찾기
    # 1. 앞단부터
    h1 = h2 = None
    for i in range(arr_len):
        if 1 in arr[i]:
            h1 = i
            break
    for i in range(arr_len-1, -1, -1):
        if 1 in arr[i]:
            h2 = i
            break

    if h1 == None or h2 == None:
        return 0

    height = (h2-h1)+1


    w1 = w2 = None
    a1 = arr[h1]
    for i in range(arr_len):
        if a1[i] == 1:
            w1 = i
            break
    for i in range(arr_len-1, -1, -1):
        if a1[i] == 1:
            w2 = i
            break

    a2 = arr[h2]
    for i in range(arr_len):
        if a2[i] == 1:
            w1 = min(w1, i)
            break
    for i in range(arr_len-1, -1, -1):
        if a2[i] == 1:
            w2 = max(w2, i)
            break

    if w1 == None or w2 == None:
        return 0
    width = w2-w1+1

    return height * width




# 음수 좌표 값 양수화를 위해 필요한 값
OFFSET = 1000

# 좌표를 배열로 표시할 때 배열의 크기(인덱스)
arr_len = OFFSET * 2 + 1

arr = [[0] * arr_len for _ in range(arr_len)]

# 첫 번재 직사각형의 좌표 : 좌표 범위 내 배열의 값 0 -> 1로 변경
x1, y1, x2, y2 = map(int, input().split())
x1 += OFFSET
y1 += OFFSET
x2 += OFFSET
y2 += OFFSET
for row in range(y1, y2):
    for col in range(x1, x2):arr[row][col] = 1

# 두 번째 직사각형의 좌표 : 좌표 볌위 내 배열의 값 1 -> 0로 변경
x1, y1, x2, y2 = map(int, input().split())
x1 += OFFSET
y1 += OFFSET
x2 += OFFSET
y2 += OFFSET
for row in range(y1, y2):
    for col in range(x1, x2): arr[row][col] = 0

answer = solution()

print(answer)