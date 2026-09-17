def solution(a, b, c):
    for i in range(a, b+1):
        if i % c == 0:
            return "NO"
    return "YES"

a, b, c = map(int, input().split())
print(solution(a,b,c))
