str = input()
arr = []
for s in str:
    if ord("A") <= ord(s) <= ord("Z"):
        arr.append(s)
    elif ord("a") <= ord(s) <= ord("z"):
        gap = ord(s) - ord("a")
        arr.append(chr(ord("A") + gap))
        
print("".join(arr))