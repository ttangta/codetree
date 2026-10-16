s = input()
answer = ""
for i in range(len(s)):
    if i % 2 == 1:
        answer += s[i]
print(answer[::-1])