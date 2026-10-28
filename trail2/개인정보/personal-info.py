class Human:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

    def info(self):
        print(f"{self.name} {self.tall} {self.weight:.1f}")

arr = []

def solution_name(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:x.name)
    print("name")
    return answer
def solution_tall(arr):
    answer =arr.copy()
    answer.sort(key=lambda x:-x.tall)
    print("height")
    return answer

for _ in range(5):
    name, tall, weight = input().split()
    tall = int(tall)
    weight = float(weight)

    arr.append(Human(name, tall, weight))

answer_name = solution_name(arr)
for a in answer_name:
    a.info()
print()

answer_tall = solution_tall(arr)
for a in answer_tall:
    a.info()