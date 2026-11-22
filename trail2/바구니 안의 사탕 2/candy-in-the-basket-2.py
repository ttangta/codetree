import sys
def solution(K):
    # 최대값을 구해야 하므로 최초 값은 시스템이 나타낼 수 있는 가장 작은 값으로 지정
    answer = -sys.maxsize

    # 전채 반복 횟수를 0+K 에서 시작하여 101-k -1 까지 지정하여 i의 앞뒤 범위를 확보
    for i in range(200, 301):
        part = arr[i-K:(i+K)+1]

        answer = max(answer, sum(part))

    return answer

N, K =  map(int, input().split())

arr = [0] * 501

for _ in range(N):
    a,x = map(int, input().split())
    arr[x+200] += a

answer = solution(K)
print(answer)