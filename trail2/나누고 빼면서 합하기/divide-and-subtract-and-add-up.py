def solution(M):
    positions = []

    while M >= 1:
        positions.append(M)
        if M % 2 == 0:
            M //= 2
        else:
            M -= 1
    answer = 0

    for p in positions:
        answer += arr[p-1]

    return answer

N, M = map(int, input().split())

arr = list(map(int, input().split()))[:N]

print(solution(M))