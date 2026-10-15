arr = ["apple", "banana", "grape", "blueberry", "orange"]
c = input()
cnt = 0
for s in arr:
    if s.find(c, 2) == 2 or s.find(c, 2) == 3:
        print(s)
        cnt += 1
print(cnt)