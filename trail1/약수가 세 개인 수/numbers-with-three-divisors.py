start, end = map(int, input().split())

answer = 0

for i in range(start, end+1):
    num = i
    cnt = 0 # 각 숫자에 대한 약수의 수를 세는 변수
    for j in range(1, num+1):
        if num % j == 0:
            cnt += 1
    if cnt == 3:
        answer += 1

print(answer)