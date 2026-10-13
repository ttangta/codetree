s1 = input()
s2 = input()
s3 = input()

n1, n2, n3 = len(s1), len(s2), len(s3)

max_v = max(n1, n2, n3)
min_v = min(n1, n2, n3)
print(max_v - min_v)