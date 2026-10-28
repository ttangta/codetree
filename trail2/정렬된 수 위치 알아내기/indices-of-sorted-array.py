# 입력 순서 = idx, 입력 값 = value
class Element1:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value

    def info(self):
        print(f"idx: {self.idx}, value: {self.value}")



def solution(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:x.value)
    return answer

n = int(input())

element = list(map(int, input().split()))[:n]

arr = []
# 입력받은 값 만큼 반복하면서 객체 생성 & 배열에 담기
for idx ,e in enumerate(element, start=1):
    arr.append(Element1(idx, e))

half_answer = solution(arr)

answer = [0] * n

for idx ,a in enumerate(half_answer, start=1):
    answer[a.idx-1] = idx

print(*answer)
