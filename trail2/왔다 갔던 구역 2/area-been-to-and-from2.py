OFFSET = (100 * 10) * 2 + 1
# 수직선을 나타내는 배열
arr = [0] * OFFSET

# 시작 위치를 배열의 중간에서부터 시작
current = OFFSET // 2

N = int(input())

for _ in range(N):
    x, c = input().split()
    x = int(x)

    # 오른쪽으로 이동하는 경우
    if c == 'R':
        # 구간을 나타내는 방법 i ~ (i-1) 값 1 증가
        for i in range(current, (current+x)):
            arr[i] += 1
        # 종료 후 위치 이동 -> current + x
        current += x
    # 왼쪽으로 이동하는 경우
    else:
        for i in range(current-1, (current-x)-1, -1):
            arr[i] += 1
        current -= x

answer = 0

for a in arr:
    if a >= 2: answer += 1

print(answer)