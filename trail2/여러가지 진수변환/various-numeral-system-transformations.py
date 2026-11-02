def solution(N, B):
    arr = []
    while N > 0:
        arr.append(N%B)
        N //= B

    answer = 0
    for i in range(len(arr)-1, -1, -1):
        answer = answer * 10 + arr[i]

    return answer
N, B = map(int, input().split())

print(solution(N, B))