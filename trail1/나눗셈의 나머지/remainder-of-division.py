A, B = map(int, input().split())

arr_cnt = [0] * 10

# A가 1 초과인 경우 반복
while A > 1:
    num2 = A % B
    arr_cnt[num2] += 1

    A //= B

sum_v = 0

for i in range(10):
    sum_v += (arr_cnt[i] ** 2)

print(sum_v)