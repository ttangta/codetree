import sys
def gap_team():
    min_gap = sys.maxsize
    for i in range(0, 6):
        for j in range(i+1, 6):
            for k in range(j+1, 6):
                sum1 = (arr[i] + arr[j] + arr[k])
                sum2 = sum(arr) - sum1
                min_gap = min(min_gap, abs(sum1 - sum2))
    return min_gap
arr = list(map(int, input().split()))[:6]

answer = gap_team()

print(answer)