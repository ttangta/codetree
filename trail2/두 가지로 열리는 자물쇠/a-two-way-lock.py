def solution(N, c1, c2):
    # N이 5이하라면, 1~N까지로 만드는 숫자를 한 번만 반환
    if N <= 5:
        return N**3

    # 1~N 까지의 수를 값으로 가지는 배열 생성
    arr = [i+1 for i in range(N)]

    # 1번 조합의 각 자리수에서 접근 가능한 요소 구하기
    a1 = []
    for i in range(3):
        part = []
        t = c1[i]
        t_idx = None
        for idx, value in enumerate(arr):
            if t == value:
                t_idx = idx
                break
        for k in range(5):
            idx = (t_idx - 2) + k
            if idx >= N:
                idx %= N
            part.append(arr[idx])
        a1.append(part)

    # 2번 조합의 각 자리수에서 접근 가능한 요소 구하기
    a2 = []
    for i in range(3):
        part = []
        t = c2[i]
        t_idx = None
        for idx, value in enumerate(arr):
            if t == value:
                t_idx = idx
                break
        for k in range(5):
            idx = (t_idx - 2) + k
            if idx >= N:
                idx %= N
            part.append(arr[idx])
        a2.append(part)

    # 중복 요소 제거를 위한 배열
    remove = [0] * 3
    for i in range(3):
        remove[i] = 10-len(set(a1[i] + a2[i]))
    cnt = 1
    for i in remove:
        cnt *= i
    return ((5**3)*2)-cnt


N = int(input())

c1 = tuple(map(int, input().split()))
c2 = tuple(map(int, input().split()))

answer = solution(N, c1, c2)

print(answer)