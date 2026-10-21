str = input()
arr = []

for s in str:
    if ord("A") <= ord(s) <= ord("Z"):
        gap = ord(s) - ord("A")
        s = chr(ord("a") + gap)
    elif ord("a") <= ord(s) <= ord("z"):
        gap = ord(s) - ord("a")
        s = chr(ord("A") + gap)
    
    arr.append(s)

print("".join(arr))