# 명령어는 최대 1000개이고 한 번의 명령어에서 최대 이동 거리는 100
# 모든 명령어가 특정 방향으로만 최대 이동가능 거리로 이동할 경우의 거리
# 이를 L, R 모든 상황에 대입하기 위해 * 2 진행
OFFSET = (1000 * 100) * 2 + 1

# 현재 위치를 나타내는 변수
POINT = OFFSET // 2

# 타일에 칠해진 값을 나타내기 위한 리스트
CURRENT = [0] * OFFSET

# 검정, 흰색이 칠해진 횟수를 나타내는 두 리스트의 모든 인덱스의 위치가 모두 2일 때 
# 회색으로 지정하고 색 변경 생략
B_CNT = [0] * OFFSET
W_CNT = [0] * OFFSET


def solution(cmd):
    # 현재 위치를 나타내는 변수 POINT는 하나의 명령 수행 후 이동해야 하므로 global 키워드 사용
    global POINT
    global B_CNT
    global W_CNT

    # 인자로 전달 받은 명령어 만큼 반복하며 로직 수행
    for x, c in cmd:
        # 이동 방향에 따라 로직 수행
        if c == 'R': # 타일의 색을 검정으로 칠해야하는 명령
            # x의 크기만큼 반복하는 동안
            for i in range(POINT, (POINT+x)):
                # 검정으로 칠해진 이력이 1번 이상,(이번 이동에서 회색이 되기 때문), 흰색으로 칠해진 이력이 2번 이상이면 해당 위치 회색
                if B_CNT[i] >= 1 and W_CNT[i] >= 2:
                    B_CNT[i] += 1
                    CURRENT[i] = 'g'

                # 만약 현재 위치의 색이 회색이면 건너뛰기
                if CURRENT[i] == 'g': continue

                CURRENT[i] = 'b'
                B_CNT[i] += 1
            
            POINT = POINT + x - 1 

        else: # 타일의 색을 흰색으로 칠해야 하는 명령어
            # x의 크기만크 반복하는 동안
            for i in range(POINT, (POINT - x), -1):
                # 흰색으로 칠해진 이력이 1번 이상,(이번 이동에서 회색이 되기 때문), 검정으로 칠해진 이력이 2번 이상이면 해당 위치 회색 
                if B_CNT[i] >= 2 and W_CNT[i] >= 1:
                    W_CNT[i] += 1
                    CURRENT[i] = 'g'

                # 만약 현재 위치의 색이 회색이면 건너뛰기
                if CURRENT[i] == 'g': continue

                CURRENT[i] = 'w'
                W_CNT[i] += 1

            POINT = POINT - x + 1

    w = CURRENT.count('w')
    b = CURRENT.count('b')
    g = CURRENT.count('g')

    return w, b, g



# 명령의 횟수 
N = int(input())


cmd = []
for _ in range(N):
    # 이동 거리, 이동 방향
    x, c = input().split()
    x = int(x)


    # 명령어를 리스트에 담기
    cmd.append(tuple([x, c]))

# 모든 명령어를 입력받은 후 solution 함수에 전달
w, b, g = solution(cmd)

print(w, b, g)