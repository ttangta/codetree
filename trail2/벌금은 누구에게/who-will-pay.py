def solution(N, M, K, warning):
    # N명의 학생의 누적 경고 횟수를 0회로 초기화한 배열 생성
    students = [0] * N

    # 경고 정보만큼 반복하면서 해당 값의 번호의 학생에 값 1증가
    for w in warning:
        students[w-1] += 1
        if students[w-1] == K:
            return w
    return -1

N, M, K = map(int, input().split())

warning = []

for _ in range(M):
    warning.append(int(input()))


answer = solution(N, M, K, warning)

print(answer)