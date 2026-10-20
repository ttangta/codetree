s = input()
s = list(s)
base = s[0]
tmp = s[1]

for i in range(1, len(s)):
    if s[i] == tmp:
        s[i] = base

print("".join(s))