A = input()
B = input()
answer = 0
while A.find(B) != -1:
    answer += 1
    A = A[A.find(B)+1:]

print(answer)