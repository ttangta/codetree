def solution(n):
    cnt = 1
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            if cnt > 9: cnt = 1
            result[i].append(cnt)
            cnt += 1
    return result
    

N = int(input())

result = solution(N)

for r in result:
    print(*r)
