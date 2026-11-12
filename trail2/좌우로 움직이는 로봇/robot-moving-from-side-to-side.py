def movement(arr, t, d):
    # 전달받은 리스트 인자의 마지막 요소를 현재 위치로 지정
    cur = arr[-1]

    # 이동 방향에 따라 값 변경
    value = None
    # 왼쪽 이동인 경우 -1
    if d == 'L':
        value = -1
    else:
        value = 1

    # t 만큼 반복하면서 현재 값에 value를 더한 값을 배열에 추가
    for _ in range(t):
        arr.append(cur + value)
        # 한 번 이동 후 cur 값을 현재의 마지막 요소로 갱신
        cur = arr[-1]

def solution(A, B):
    a, b = len(A), len(B)
    gap = abs(a-b)
    if a < b:
        for i in range(gap):
            A.append(A[-1])
    else:
        for i in range(gap):
            B.append(B[-1])

    answer = 0
    for i in range(1, len(A)):
        if (A[i] == B[i]) and (A[i-1] != B[i-1]):answer +=1
    return answer

N, M = map(int, input().split())

A = [0]
B = [0]

for _ in range(N):
    t, d = input().split()
    t = int(t)
    movement(A, t, d)

for _ in range(M):
    t, d = input().split()
    t = int(t)
    movement(B, t, d)

answer = solution(A, B)
print(answer)