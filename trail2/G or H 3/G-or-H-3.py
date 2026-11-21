import sys
def solution(N, K):
    answer = -sys.maxsize

    for i in range(len(arr)-K+1):
        answer = max(answer, sum(arr[i:(i+K+1)]))

    return answer

N, K = map(int, input().split())

arr = [0] * 10000


for _ in range(N):
    idx, value = input().split()
    idx = int(idx)-1

    score = 0
    if value == 'G':
        score = 1
    else:
        score = 2

    arr[idx] = score

print(solution(N,K))