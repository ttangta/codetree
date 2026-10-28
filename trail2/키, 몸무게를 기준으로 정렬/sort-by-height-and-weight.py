class Humen:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def info(self):
        print(f"{self.name} {self.height} {self.weight}")


def solution(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:(x.height, -x.weight))
    return answer

n = int(input())

arr = []
for _ in range(n):
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)
    arr.append(Humen(name, height, weight))

answer = solution(arr)

for a in answer:
    a.info()