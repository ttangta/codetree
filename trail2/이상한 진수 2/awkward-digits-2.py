def solution(N):
    # 문자열은 불변객체이므로 리스트형으로 변경
    lis = list(N)

    # 정답을 정수 최소값인 0으로 초기화
    answer = 0

    for i in range(len(lis)):
        num = lis[i]
        if num == '1':
            lis[i] = '0'
        else:
            lis[i] = '1'
        answer = max(answer, int(''.join(lis), 2))
        lis[i] = num
    return answer

N = input()

print(solution(N))