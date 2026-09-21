n = int(input())

even_cnt = 1
odd_cnt = n
for i in range(n*2):
    if i % 2 == 0:
        print("* " * even_cnt)
        even_cnt += 1
    else:
        print("* " * odd_cnt)
        odd_cnt -= 1
print()