def solution(handshakes, K):
    # 둘 다 감염자인 경우 y의 전염 횟수가 줄어들지 않고 있음
    for h in handshakes:
        x, y = h[1], h[2]

        # 둘 다 감염자인 경우
        if status[x] and status[y]:
            counts[x] -= 1
            counts[y] -= 1
        # 한 명만 감염인 경우
        elif status[x] or status[y]:
            # y가 감염자인 경우 전염 흐름을 x ~> y로 고정하기 위해 swap
            if status[y]:
                x, y = y, x

            # 만약 x의 감염 횟수가 1이상인 경우
            # x 감염횟수 -1 -> y 상태 1 -> y 감염 횟수 K
            if counts[x] >= 1:
                counts[x] -= 1
                status[y] = 1
                counts[y] = K


N, K, P, T = map(int, input().split())

handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# 최종 감염 상태
status = [0] * (N+1)
status[P] = 1

# 잔여 전염 횟수
counts = [0] * (N+1)
counts[P] = K

# print(f'초기 전염 횟수: {counts}')
# print(f'감염자 상태: {status}')


# 시간 순으로 정렬
handshakes.sort(key=lambda x:x[0])

solution(handshakes, K)

for i in range(1, N+1):
    print(status[i], end='')