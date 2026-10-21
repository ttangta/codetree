s1, s2 = input().split()

s1 = ord(s1)
s2 = ord(s2)

if s2 > s1:
    s1, s2 = s2, s1

print((s1+s2), (s1-s2))