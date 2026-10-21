str = input()
arr = []
for s in str:
    if s.isalpha():
        if ord("A") <= ord(s) <= ord("Z"):
            gap = ord(s) - ord("A")
            s = chr(ord("a") + gap)
        arr.append(s)
    elif s.isnumeric():
        arr.append(s)

print("".join(arr))