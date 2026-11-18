def solution(N):
    answer = 0

    for i in range(N-2):
        num1 = arr[i]
        for j in range(i+1, N-1):
            num2 = arr[j]
            if num1 > num2: continue
            for k in range(j+1, N):
                num3 = arr[k]
                if num1 > num3 or num2 > num3: continue
                answer += 1
    return answer

N = int(input())
arr = list(map(int, input().split()))
print(solution(N))