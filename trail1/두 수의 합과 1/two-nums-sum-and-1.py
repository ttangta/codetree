A, B = map(int, input().split())

sum_v = str(A+B)

answer = 0
for s in sum_v:
    if s == "1": answer +=1

print(answer)