def movement(arr, d, t):
    # 현재 위치를 알아야 함 -> 가장 마지막에 추가된 값 가져오기
    cur = arr[-1]
    value = None

    # 현재 위치에서 t 만큼 반복하면서 이동 이때, 이동만 d의 값에 따라 바뀜
    for i in range(t):
        if d == 'L': value = -1
        else: value = 1
        arr.append(cur + value)
        cur = arr[-1]

def solution(A, B):
    lower = len(A)
    bigger = len(B)
    if lower > bigger:
        lower, bigger = bigger, lower
    for i in range(1, bigger):
        if A[i] == B[i]:return i
    return -1


# A가 N번 움직임, B가 M번 움직임
N, M = map(int, input().split())

A = [0]
for _ in range(N):
    d, t = input().split()
    t = int(t)
    movement(A, d, t)

B = [0]
for _ in range(M):
    d, t = input().split()
    t = int(t)
    movement(B, d, t)

answer = solution(A, B)
print(answer)
