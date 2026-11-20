def solution(N, S):
    answer = 0

    for i in range(N-2):
        if S[i] == 'C':
            for j in range(i+1, N-1):
                if S[j] == 'O':
                    for k in range(j+1,N):
                        if S[k] == 'W':
                            answer += 1
    return answer

N = int(input())
S = input()[:N]

answer = solution(N, S)

print(answer)