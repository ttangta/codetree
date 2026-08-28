N = int(input())
result = ''
for i in range(1, N+1):
    if i%2==0 or i%3==0:
        result += str(1) + ' '
    else:
        result += str(0) + ' '
print(result)