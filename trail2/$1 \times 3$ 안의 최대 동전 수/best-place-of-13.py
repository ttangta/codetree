import sys
def solution(N):
    answer = -sys.maxsize

    for i in range(N):
        a = arr[i]
        for j in range(N-2):
            cnt = 0
            for k in range(j, j+3):
                if a[k] == 1:cnt+=1
            answer = max(answer, cnt)

    return answer

N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

print(solution(N))