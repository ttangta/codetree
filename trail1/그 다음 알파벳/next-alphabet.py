c = input()
c = ord(c)

if c == ord("z"):
    c = ord("a")
else:
    c += 1

print(chr(c))