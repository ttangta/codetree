def solution(N):
    answer = N

    for i in range(N-1):
        for j in range(i+1, N):
            part = num[i:j+1]
            avg = sum(part) / len(part)
            if avg in part: answer+=1

    return answer

N = int(input())

num = list(map(int, input().split()))[:N]

answer = solution(N)

print(answer)