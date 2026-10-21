c = input()
c = ord(c)

if c == ord("a"):
    c = ord("z")
else:
    c -= 1

print(chr(c))