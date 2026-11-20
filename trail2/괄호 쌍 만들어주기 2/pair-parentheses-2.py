def solution(A):
    answer = 0
    # 문자열의 길이
    N = len(A)

    # 앞단 문자가 '((' 인지 확인하기 위한 범위 조정
    # 이후 뒷단 문자가 '))' 인지 확인하기위해 탐색 범위 조정 중요
    # i가 '(' 일때 i+1도 '(' 값인지 검사 필요 이때문에 i+1도 (N-2) 인덱스에 접근하지 못하는 범위로 조정
    for i in range(N-3):
        if A[i] == '(' and A[i+1] == '(':
            for j in range(i+2, N-1):
                if A[j] == ')' and A[j+1] == ')':
                    answer += 1


    return answer

A = input()

answer= solution(A)

print(answer)