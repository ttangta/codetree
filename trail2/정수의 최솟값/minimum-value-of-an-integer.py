def solution(a, b, c):
    return min([a, b, c])


a, b, c = map(int, input().split())
print(solution(a,b,c))