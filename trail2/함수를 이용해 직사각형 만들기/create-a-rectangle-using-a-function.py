def solution(n, m):
    arr = [[1] * m for _ in range(n)]
    return arr

n, m = map(int, input().split())

result = solution(n, m)
for r in result:
    print(*r, sep="")