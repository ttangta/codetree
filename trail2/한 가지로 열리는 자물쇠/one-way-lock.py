def solution(N, base):
    answer = N * N * N
    arr = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if abs(base[0] - i) <= 2 or abs(base[1] - j) <=2 or abs(base[2] - k) <= 2:
                    part = [i, j, k]
                    arr.append(part)
    return len(arr)



N = int(input())

base = tuple(map(int, input().split()))

answer = solution(N, base)

print(answer)