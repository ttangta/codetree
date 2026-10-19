s = input()
s = list(s)
s[1] = "a"
s[-2] = "a"
s = "".join(s)
print(s)