s, Q = input().split()
Q = int(Q)
n = len(s)
for _ in range(Q):
    q = int(input())
    if n == 1:
        print(s)
        continue
    if q == 1:
        s = s[1:] + s[0]
    elif q == 2:
        s = s[-1] + s[:(n-1)]
    elif q == 3:
        arr = [0] * n
        # s의 길이가 홀수 일 때
        if n%2 !=0:
            for i in range(n//2):
                e = n-1-i
                arr[i] = s[e]
                arr[e] = s[i]
            arr[n//2] = s[n//2]
        # s의 길이가 짝수 일 때
        else:
            for i in range(n//2):
                e = n-1-i
                arr[i] = s[e]
                arr[e] = s[i]
        s = "".join(arr)

    print(s)