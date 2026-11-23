def solution(N):
    answer = 0

    # 사람이 한 명만 있는 경우 크기는 무조건 0
    if N <= 1: return answer

    # 0 ~ 99 인덱스까지 접근 -> 99번 인덱스에 도착 시 100번 인덱스도 비교하기 위해
    for i in range(100):
        # 배열의 i번째 값이 0이 아닌 경우
        if arr[i] != 0:
            g = h = 0
            c1 = arr[i]
            g_idx = h_idx = 0
            if c1 == 'G': g+=1
            else: h += 1
            # i번째 이후 인덱스 접근
            for j in range(i+1, 101):
                if arr[j] == 0: continue
                else:
                    c2 = arr[j]
                    if c2 == 'G':
                        g+=1
                        g_idx = j
                    else:
                        h += 1
                        h_idx = j
                    # 만약 'G' 와 'H'가 동일하게 등장한 경우
                    if g == h: answer = max(answer, j - i)
            # 만약 내부 반복문을 모두 순회했을 때 동일한 문자만 존재하는 경우
            if g >= 1 and h == 0:
                answer = max(answer, g_idx - i)
            elif h >= 1 and g == 0:
                answer = max(answer, h_idx - i)
    return answer
N = int(input())

arr = [0] * 101

for _ in range(N):
    x, c = input().split()
    x = int(x)
    arr[x] = c

answer = solution(N)
print(answer)