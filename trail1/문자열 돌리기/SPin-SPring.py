s = input()
L = len(s)

for _ in range(L+1):
    print(s)
    s = s[-1] + s[:(L-1)]