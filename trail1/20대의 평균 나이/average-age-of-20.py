arr = []
while True:
    n = int(input())

    if 20<=n<=29:
        arr.append(n)
    
    else:
        result = sum(arr)/len(arr)
        print(f"{result:.2f}")
        break