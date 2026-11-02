def solution(N):
    arr = []
    while N > 0:
        arr.append(N%2)
        N //= 2
    answer = 0
    for i in range(len(arr)-1, -1, -1):
        answer *= 10
        answer += arr[i]

    return answer


N = int(input())

print(solution(N))