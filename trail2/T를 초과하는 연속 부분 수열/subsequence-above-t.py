def solution(N, T, arr):
    answer = 0

    # 연속 부분 수열의 길이 기본값 0으로 지정
    cnt = 0

    # N만큼 반복하는 동안
    for i in range(N):
        # i가 0번이면서 arr[0]의 값이 T 보다 크면 cnt 값 1 증가
        if i == 0 and arr[i] > T:
            cnt += 1
        # 만약 i가 1 이후이면서 arr[i]의 값이 T 보다 크면 cnt 값 1 증가
        elif arr[i] > T:
            cnt += 1
        # 그게 아니라면 현재 부분수열의 길이 중 가장 긴 값을 정답으로 하고 cnt를 0으로 초기화
        else:
            answer = max(answer, cnt)
            cnt = 0

    # arr의 모든 요소가 T보다 큰 경우 answer 값을 갱신하는 코드가 호출이 안되므로 반복문 밖에서 answer 값 갱신 한 번 더 실행
    answer = max(answer, cnt)

    return answer

N, T = map(int, input().split())

arr = list(map(int, input().split()))[:N]

print(solution(N, T, arr))