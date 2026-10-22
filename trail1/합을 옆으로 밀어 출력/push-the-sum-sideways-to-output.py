t = int(input())
sum_v = 0
for _ in range(t):
    sum_v += int(input())
    
answer = str(sum_v)
answer = answer[1:] + answer[0]

print(answer)