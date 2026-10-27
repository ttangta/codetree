class Student:
    def __init__(self, tall, weight, no):
        self.tall = tall
        self.weight = weight
        self.no = no

    def info(self):
        print(f"{self.tall} {self.weight} {self.no}")

def solution(arr):
    arr.sort(key=lambda x:(-x.tall, -x.weight, x.no))
n = int(input())
arr = []
for i in range(1, n+1):
    tall, weight = map(int, input().split())
    arr.append(Student(tall, weight, i))


solution(arr)

for a in arr:
    a.info()