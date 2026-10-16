A = input()
cnt = 1
answer = ""
for i in range(len(A)-1):
    if A[i] == A[i+1]:cnt+=1
    else:
        answer += A[i] + str(cnt)
        cnt = 1
answer += A[len(A)-1] + str(cnt)

print(len(answer))
print(answer)