class POINT:
    def __init__(self, no, x, y):
        self.no = no
        self.x = x
        self.y = y

def solution(arr):
    answer = []
    arr.sort(key=lambda p:(abs((p.x-0)) + abs((p.y-0)), p.no))
    for a in arr:
        answer.append(a.no)
    return answer
arr = []
n = int(input())

for i in range(1, n+1):
    x, y = map(int, input().split())
    arr.append(POINT(i, x, y))

answer = solution(arr)
for a in answer:
    print(a)
