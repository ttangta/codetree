s = input()

idx = s.find("e")

s = list(s)

s.pop(idx)

s = "".join(s)

print(s)