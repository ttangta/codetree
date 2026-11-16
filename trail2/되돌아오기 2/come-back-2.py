DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

def solution(s):
    # 최초 좌표로 돌아오기 까지 걸리는 시간 즉, 정답
    time = 0

    # 입력받은 문자열들을 리스트로 변환하여 각각의 명령어에 대한 동작을 수행한다.
    cmd = list(s)

    # 최초 위치 좌표 값 지정
    cur_x = cur_y = 0

    # 현재 이동 방향 값 초기화
    dir = 0

    for c in cmd:
        if c == 'F':
            cur_x = cur_x + DX[dir]
            cur_y = cur_y + DY[dir]
        elif c == 'R':
            dir = (dir+1) % 4
        elif c == 'L':
            dir = (4 - 1 + dir) % 4

        time += 1

        if cur_x == 0 and cur_y == 0: return time

    return -1


s = input()
answer = solution(s)
print(answer)