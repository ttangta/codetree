arr = list(map(int, input().split()))

for a in arr:
    if not a:
        break
    
    if a % 2 == 0:
        print(a//2, end = " ")
    else:
        print(a+3, end = " ")

