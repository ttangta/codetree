arr = ["L", "E", "B", "R", "O", "S"]


chr = input()

idx = -1
for i, c in enumerate(arr):
    if c == chr:
        idx = i
        break


if idx == -1:
    print(None)
else:
    print(idx)