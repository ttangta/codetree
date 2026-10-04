n = int(input())

base = 1 # 최초 배수의 수
cnt = 0 # 5의 배수가 2번 출력되면 프로그램 종료

arr = []
while True:
    # n의 배수를 리스트에 저장
    num = n * base
    arr.append(num)

    if num%5 == 0:
        cnt += 1

    if cnt == 2:
        break    
    
    # 배수의 수 1 증가
    base += 1

print(*arr)