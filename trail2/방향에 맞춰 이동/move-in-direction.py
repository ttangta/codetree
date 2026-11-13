DX = [-1, 0, 0, 1]
DY = [0, -1, 1, 0]
def solution(cmd):
    x = y = 0
    for c in cmd:
        idx = None
        if c[0] == 'W':
            idx = 0
        elif c[0] == 'S':
            idx = 1
        elif c[0] == 'N':
            idx = 2
        elif c[0] == 'E':
            idx = 3

        cnt = int(c[1])
        for i in range(cnt):
            x += DX[idx]
            y += DY[idx]

    return x, y


N = int(input())

cmd = [tuple(input().split()) for _ in range(N)]

x, y = solution(cmd)
print(x, y)