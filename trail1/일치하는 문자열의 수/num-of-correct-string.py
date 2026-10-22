n, A = input().split()
n = int(n)

answer = 0
for _ in range(n):
    s = input()
    if A == s: answer += 1
    
print(answer)