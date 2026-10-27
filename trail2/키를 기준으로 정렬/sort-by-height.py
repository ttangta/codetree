class Humen:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

    def info(self):
        print(f"{self.name} {self.tall} {self.weight}")

def solution(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:x.tall)

    return answer

n = int(input())
arr = []
for _ in range(n):
    s = input().split()
    name = s[0]
    tall = int(s[1])
    weight = int(s[2])

    arr.append(Humen(name, tall, weight))

answer = solution(arr)

for a in answer:
    a.info()