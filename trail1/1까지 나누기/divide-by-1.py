def solution(n):
    i = 1
    while True:
        n = n // i 
        if n <= 1:
            break
        i += 1
    return i

n = int(input())
print(solution(n))