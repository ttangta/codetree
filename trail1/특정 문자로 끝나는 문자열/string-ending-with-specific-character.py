arr = []

for _ in range(10):
    arr.append(input())

c = input()

is_exist = False
for a in arr:
    if a[-1] == c:
        is_exist = True
        print(a)
        
if not is_exist:
    print(None)