def solution(N, arr):
    answer = 1
    cnt = 1

    for i in range(N):
        if i == 0 or arr[i] <= arr[i-1]:
            answer = max(answer , cnt)
            cnt = 1
        else:
            cnt += 1


    answer = max(answer , cnt)
    
    return answer

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

print(solution(N,arr))