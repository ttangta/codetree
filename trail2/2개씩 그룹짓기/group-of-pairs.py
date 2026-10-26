def solution(n, arr):
    arr.sort()
    answer = arr[0] + arr[2*n-1]
    for i in range((n*2)//2):
        answer = max(answer, arr[i] + arr[(2*n-1)-i])
    return answer        

n = int(input())
arr = list(map(int, input().split()))[:(2*n)]
print(solution(n, arr))