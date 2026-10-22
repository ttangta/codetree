A = input()
B = input()

origin = A
cnt = 0

while True:
    # A를 우측으로 밀기 전 현재 A와 B가 같은지 비교
    if A == B: break
    
    A = A[-1] + A[:-1]
    cnt += 1
    if A == origin:
        cnt = -1
        break
print(cnt)