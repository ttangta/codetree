s1 = input()
s2 = input()

for i in range(len(s1)):
    if s1[i] == " ":
        continue
    print(s1[i], end = "")
for i in range(len(s2)):
    if s2[i] == " ":
        continue
    print(s2[i], end = "")