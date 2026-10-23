def c1(n):
    # 소수가 아니면 False 반환
    for i in range(2, n):
        if n % i == 0:return False
    return True
def c2(n):
    arr = map(int, list(str(n)))

    return (sum(arr)) % 2 == 0


A, B = map(int, input().split())

cnt = 0

for i in range(A, B+1):
    if c1(i):
        if c2(i):
            cnt += 1
print(cnt)
