cnt = 0
words = []
while True:
    s = input()
    
    if s == '0':break
    
    if cnt % 2 == 0: words.append(s)
    
    cnt += 1
    
print(cnt)
for w in words:
    print(w)