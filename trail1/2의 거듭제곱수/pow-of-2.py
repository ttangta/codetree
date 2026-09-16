def solution(n):
    cnt = 0

    # 짝수가 아닌 값은 바로 리턴
    if n % 2 != 0:
        return -1

    while True:
        n //= 2
        if n == 0:
            break
        cnt += 1
    return cnt

n = int(input())
print(solution(n))
