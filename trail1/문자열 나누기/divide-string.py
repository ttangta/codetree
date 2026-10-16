n = int(input())

arr = input().split()

answer = ""

for a in arr:
    for i in range(len(a)):
        answer += a[i]
        if len(answer) == 5:
            print(answer)
            answer = ""
print(answer)