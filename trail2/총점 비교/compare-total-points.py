class Humen:
    def __init__(self, name, ko, en, math):
        self.name = name
        self.ko = ko
        self.en = en
        self.math = math
    def info(self):
        print(f"{self.name} {self.ko} {self.en} {self.math}")

def solution(arr):
    answer = arr.copy()

    answer.sort(key=lambda x: (x.ko + x.en + x.math))

    return answer

n = int(input())
arr = []
for _ in range(n):
    s = input().split()
    name = s[0]
    ko = int(s[1])
    en = int(s[2])
    math = int(s[3])
    arr.append(Humen(name, ko, en, math))

answer = solution(arr)

for a in answer:
    a.info()