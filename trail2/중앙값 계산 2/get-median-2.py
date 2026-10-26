def solution(answer):
    answer.sort()
    
    N = len(answer)//2
    return answer[N]

n = int(input())

arr = list(map(int, input().split()))[:n]

answer = []
for i in range(n):
    answer.append(arr[i])
    if i % 2 == 0:
        print(solution(answer), end = " ")
print()
        