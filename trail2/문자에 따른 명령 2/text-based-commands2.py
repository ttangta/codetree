def solution(cmd):
    x = y = 0

    dir = 3

    for c in cmd:
        if c == 'R':
            dir = (dir + 1) % 4
        elif c == 'L':
            dir = (4 - 1 + dir) % 4
        elif c == 'F':
            if dir == 3: y += 1
            elif dir == 2: x -= 1
            elif dir == 1: y -= 1
            elif dir == 0: x += 1

    return x, y

cmd = list(input())

x, y = solution(cmd)

print(x, y)
