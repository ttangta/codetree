n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    
    sum_v = 0
    
    for i in range(a, b+1):
        if i % 2 == 0:sum_v += i
    
    print(sum_v)