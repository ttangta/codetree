N = int(input())

prices = list(map(int, input().split()))[:N]
answer = 0


for i in range(N-1):
    for j in range(i+1, N):
        if prices[i] > prices[j]:continue
        elif prices[i] < prices[j]:
            benefit = prices[j]-prices[i]
            answer = max(answer, benefit)

print(answer)