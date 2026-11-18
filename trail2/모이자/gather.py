import sys

def solution(N, arr):
    answer = sys.maxsize
    for i in range(N):
        sum = 0
        for j in range(N):
            gap = abs(i - j)
            sum += arr[j] * gap
        answer = min(answer, sum)

    return answer

N = int(input())
arr = list(map(int, input().split()))

print(solution(N, arr))