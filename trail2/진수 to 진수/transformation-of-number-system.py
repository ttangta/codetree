def solution(A, B, N):
    if N == '0': return N

    N = list(map(int, list(N)))

    num = 0
    for n in N:
        num = num * A + n

    arr = []
    while num > 0:
        arr.append(num%B)
        num //= B

    arr = list(map(str,arr[::-1]))
    answer = "".join(arr)
    return answer

A, B = map(int, input().split())
N = input()

print(solution(A, B, N))