def solution(a, b, c):
    # 일이 제약조건에 위배 되면 -1 리턴
    if a < 11 or a > 14: return -1

    # 분이 11보다 작다면
    if c < 11:
        # b를 1 감소 시킨 후 c에 60 더해주기
        b -= 1
        c += 60
        c -= 11

    # 분이 11 이상 이라면
    else:
        c -= 11

    # 시가 11보다 작다면
    if b < 11:
        # a를 1 감소 시킨 후 b에 24 더해주기
        a -= 1
        b += 24
        b -= 11
    # 시가 11 이상 이라면
    else:
        b -= 11

    a -= 11

    if a < 0:
        return -1

    answer = (a * 24 * 60) + (b * 60) + c

    return answer


a,b,c = map(int, input().split())

print(solution(a,b,c))