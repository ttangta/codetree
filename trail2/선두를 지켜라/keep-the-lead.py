def movement(arr ,v, t):
    # 함수 호출 시 인자로 전달받은 리스트의 마지막 요소를 현재 값으로 가정
    cur = arr[-1]

    # 인자로 전달받은 t 시간동안 현재 위치에서 v만큼 이동
    for i in range(t):
        # v 만큼 이동한 값을 다음 시간대(인덱스) 값으로 추가
        next = cur + v
        arr.append(next)
        # cur을 가장 최근에 추가된 값으로 갱신
        cur = arr[-1]

def solution(A, B):
    # 최초로 두 배열의 값이 다른 곳을 시작 지점으로 초기화
    point = None
    flag = None
    for i in range(len(A)):
        if A[i] != B[i]:
            point = i
            if A[i] > B[i]: flag = 'A'
            else: flag = 'B'
            break

    answer = 0
    # 최초 시작 지점부터 끝까지 반복하면서 각 인덱스에 대한 값 비교 현재 flag가 변경되는 경우 answer 값 1 증가
    for i in range(i, len(A)):
        if flag == 'A':
            if A[i] < B[i]:
                answer += 1
                flag = 'B'
        else:
            if A[i] > B[i]:
                answer += 1
                flag = 'A'

    return answer

N, M = map(int, input().split())

A = [0]
B = [0]
for _ in range(N):
    v, t = map(int, input().split())
    movement(A, v, t)

for _ in range(M):
    v, t = map(int, input().split())
    movement(B, v, t)
print(solution(A, B))