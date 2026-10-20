s = input()

while len(s) != 1:
    s = list(s)
    n = int(input())
    if n >= len(s):
        s.pop()
    else: s.pop(n)
    print("".join(s))