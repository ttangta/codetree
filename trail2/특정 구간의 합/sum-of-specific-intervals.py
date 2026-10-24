def solution(a1, a2):
    answer = sum(A[a1-1:a2])
    return answer

N, M = map(int, input().split())

A = list(map(int, input().split()))[:N]

for _ in range(M):
    a1, a2 = map(int, input().split())

    print(solution(a1, a2))