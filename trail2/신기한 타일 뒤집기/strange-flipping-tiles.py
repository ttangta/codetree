# 명령어의 최대 개수 = 1000, 각 명령어를 통해 한 번에 이동 가능한 최대 이동 거리 = 100
# 이때, 모든 명령어가 한 쪽 방향으로만 이동할 경우 모든 명령어 수행 후 도달하는 인덱스 값 이를 양단으로 지정
OFFSET = (1000 * 100) * 2 + 1

# 각 위치의 현재 색을 나타내는 리스트
CURRENT = [0] * OFFSET

# 현재 위치를 나타내는 변수
POINT = OFFSET // 2


def solution(cmd):
    w = b = 0

    # 명령어 수행 후 POINT의 값을 변경해야하기 때문에 전역변수 POINT에 global 키워드 붙힘
    global POINT

    # 명령어 만큼 반복하면서 각 명령어에 해당하는 색으로 변경
    for x, c in cmd:
        # 오른쪽 이동인 경우 -> 검정색 
        if c == 'R':
            for i in range(POINT, (POINT + x)):
                CURRENT[i] = 'b'
            # 해당 방향 범위에 모두 지정된 명령 수행 후 POINT 값 변경
            POINT = POINT + x -1

        # 왼쪽 이동인 경우 -> 흰색
        else:
            for i in range(POINT, (POINT - x), -1):
                CURRENT[i] = 'w'
            # 해당 방향 범위에 모든 지정된 명령 수행 후 POINT 값 변경
            POINT = POINT - x + 1

    w = CURRENT.count('w')
    b = CURRENT.count('b')

    return w, b

N = int(input())

cmd = []

for _ in range(N):
    # 이동 거리, 이동 방향
    x, c = input().split()
    # 이동 거리를 정수형으로 타입 변형
    x = int(x)

    # 각 명령어를 cmd 리스트에 튜플 형식으로 추가
    cmd.append(tuple([x, c]))


# 명령어 입력이 끝난다면, 함수 호출
w, b = solution(cmd)

print(w, b)