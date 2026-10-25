def solution(level, mul):
    if level == N-1:
        if mul % arr[level] == 0: return mul
        else:
            for i in range(2, arr[level]):
                if (mul * i) % arr[level] == 0: return (mul * i)
            return mul * arr[level]

    # 다음번 요소의 값
    next = arr[level+1]

    # 만약 현재 공배수%next == 0이면 현재 공배수로 나누어 떨어진다는 것
    if mul % next == 0:
        return solution(level+1, mul)
    # 만약 나누어 떨어지지 않는다면 현재 공배수에 다음 요소 2~next-1까지 나누어 떨어지는 값이 있는지 확인
    else:
        for i in range(2, next):
            if (mul*i) % next == 0: return solution(level+1, (mul*i))
        return solution(level+1, (mul * next))


N = int(input())
arr = list(map(int, input().split()))[:N]

print(solution(0, arr[0]))