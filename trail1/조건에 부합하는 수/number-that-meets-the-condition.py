def solution(n):
    result = []
    for i in range(1, n+1):
        if (i % 2 == 0 and i % 4 != 0) or i//8%2 == 0 or i % 7 < 4:
            continue
            
        result.append(i)

    return result

n = int(input())
print(*solution(n))