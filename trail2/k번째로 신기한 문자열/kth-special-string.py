def solution(arr, K):
    arr.sort()
    return arr[K-1]

N, K, T = input().split()

N = int(N)
K = int(K)
arr = []
for _ in range(N):
    s = input()
    if s.startswith(T):
        arr.append(s)
    
print(solution(arr, K))