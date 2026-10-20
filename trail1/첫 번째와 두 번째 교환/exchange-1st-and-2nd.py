s = input()

s = list(s)
t1 = s[0]
t2 = s[1]

for i in range(len(s)):
    if s[i] == t1:
        s[i] = t2
    elif s[i] == t2:
        s[i] = t1

s = "".join(s)

print(s)