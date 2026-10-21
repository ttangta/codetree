A = input()
sum_v = 0
for a in A:
    if a.isnumeric():
        sum_v += int(a)

print(sum_v)