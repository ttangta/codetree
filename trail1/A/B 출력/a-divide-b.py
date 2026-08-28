A, B = map(int, input().split())
result = str(A//B) + "."
remainder = A % B
for _ in range(20):
    remainder *= 10
    result += str(remainder//B)
    remainder %= B
print(result)