class Human:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city
    def info(self):
        print(f"name {self.name}")
        print(f"addr {self.addr}")
        print(f"city {self.city}")
def solution(n):
    answer = arr.copy()
    answer.sort(key=lambda x:x.name)
    return answer[n-1]

arr = []
n = int(input())

for _ in range(n):
    name, addr, city = input().split()
    arr.append(Human(name, addr, city))

answer = solution(n)
answer.info()