def solution(N, M):
    answer = 0

    # B 배열 요소의 값을 인덱스 번호로 하는 카운트 배열 생성 (B의 요소의 값 범위는 1~100 이를 인덱스로 나타내기 위해 0~100의 인덱스를 가질 수 있는 크기 지정)
    count = [0] * 101
    for elem in B:
        count[elem] += 1

    # 배열 A에서 M 크기의 부분 수열을 만들기 위한 반복 범위 지정
    for i in range(N-M+1):
        # A에서 부분 수열 추출
        part = A[i:i+M]
        # count 배열의 복사본 -> A의 매 부분수열과 비교하기 위해 각 A의 부분수열마다 초기화된 count 배열의 값이 필요하기 때문
        comp = count.copy()
        for p in part:
            comp[p] -= 1
        # 부분수열의 원소를 반복하는 동안 count 배열의 복사본 배열의 값을 모두 제거했다면 해당 부분수열의 원소가 모두 B배열의 '아름다운 수열' 내 원소라는 뜻
        if comp.count(0) == len(comp):
            answer += 1

    return answer

N, M = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

answer = solution(N, M)
print(answer)