s1, s2 = input().split()


tmp = s1[0:2]

s2 = list(s2)

for i in range(2):
    s2[i] = tmp[i]

s2 = "".join(s2)

print(s2) 