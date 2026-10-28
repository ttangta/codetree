class Student:
    def __init__(self, no, height, weight):
        self.no = no
        self.height = height
        self.weight = weight
    def info(self):
        print(f"{self.height} {self.weight} {self.no}")
n = int(input())

def solution(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:(x.height, -x.weight))

    return answer


arr = []
for i in range(1, n+1):
    height, weight = map(int, input().split())
    arr.append(Student(i, height, weight))


answer = solution(arr)
for a in answer:
    a.info()