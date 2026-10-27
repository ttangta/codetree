class Mem:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def solution(arr):
    return arr[0]

arr = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    m = Mem(name, score)
    arr.append(m)

arr.sort(key=lambda x:x.score)

m = solution(arr)
print(m.name, m.score)