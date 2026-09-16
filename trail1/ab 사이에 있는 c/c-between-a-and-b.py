def solution(a,b,c):
    satisfied = False

    for i in range(a, b+1):
        if i % c == 0:
            satisfied = True
            break
    
    if satisfied:
        return "YES"
    else:
        return "NO"


a, b, c = map(int, input().split())
print(solution(a,b,c))