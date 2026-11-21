def solution(N):
    answer = 0

    for r1 in range(N):
        # r1행에서 요소 3개를 슬라이싱 할 때 반드시 슬라이싱될 요소가 3개가 될 수 있는 최대 인덱스로 범위 조정
        for c1 in range(N-2):
            b1_s = c1
            b1_e = b1_s+3
            box1 = arr[r1][b1_s:b1_e]

            # 현재 r1행에서 추가적으로 박스를 배치할 수 있는 조건
            if N - (b1_s+3) >= 3:
                for c2 in range(b1_s+3, N):
                    if len(arr[r1][c2:c2+3]) == 3:
                        box2 = arr[r1][c2:c2+3]
                        answer = max(answer, (box1.count(1) + box2.count(1)))

            for r2 in range(r1+1, N):
                for c2 in range(N-2):
                    box2 = arr[r2][c2:c2+3]
                    answer = max(answer, (box1.count(1) + box2.count(1)))


    return answer

N = int(input())

arr = [list(map(int, input().split()))[:N] for _ in range(N)]

answer = solution(N)
print(answer)