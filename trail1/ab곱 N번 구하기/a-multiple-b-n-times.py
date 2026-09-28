# a~b 까지의 곱을 n번 수행하기 위한 입력
n = int(input())

# n번 반복
for _ in range(n):
    # 사용자에게 두 수를 공백 기준으로 입력 받아 각각 a, b에 할당
    a, b = map(int, input().split())

    # 답이 될 곱셈의 최초값은 1로 각 반복이 시작 시 매번 초기화가 진행되어야 함
    mul_v = 1

    # a~b의 범위 반복 지정
    for i in range(a, b+1):
        # 반복되는 값을 초기값에 곱해줌
        mul_v *= i

    print(mul_v)
