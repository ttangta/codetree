# 움직임의 결과의 값을 대입하는 함수
def mk_arr(arr, cmd):
    cur = arr[-1]

    v, t = cmd[0], cmd[1]

    for i in range(t):
        arr.append(cur+v)
        cur = arr[-1]

def solution(A, B):
    # 두 배열의 길이가 다를 경우 짧은 쪽을 긴 배열의 길이와 맟주기 위한 작업
    gap = 0
    target = None
    if len(A) != len(B):
        gap = len(A) - len(B)
        # A - B = 음수 = B가 더 긴경우
        if gap < 0:
            target = A
            gap *= -1
        target = B
    if target != None:
        increase_elm = target[-1]
        for i in range(gap):
            target.append(increase_elm)

    history = []
    for i in range(1, len(A)):
        arr = []
        if A[i] > B[i]:
            arr.append('A')
        elif A[i] < B[i]:
            arr.append('B')
        elif A[i] == B[i]:
            arr.extend(['A', 'B'])

        history.append(arr)

    answer = 1
    for i in range(1, len(history)):
        if history[i] != history[i-1]:answer += 1

    return answer

N, M = map(int, input().split())

A = [0]
B = [0]

for _ in range(N):
    cmd = tuple(map(int, input().split()))
    mk_arr(A, cmd)

for _ in range(M):
    cmd = tuple(map(int, input().split()))
    mk_arr(B, cmd)

answer = solution(A, B)
print(answer)