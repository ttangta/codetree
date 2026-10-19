s = input()

S1 = "ee"
S2 = "eb"

s_1 = s
cnt_1 = 0
while s_1.find(S1) != -1:
    cnt_1+=1
    s_1 = s_1[s_1.find(S1)+1:]

s_2 = s
cnt_2 = 0
while s_2.find(S2) != -1:
    cnt_2+=1
    s_2 = s_2[s_2.find(S2)+1:]
print(cnt_1, cnt_2)
