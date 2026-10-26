def solution(s1, s2):
    s1 = list(s1)
    s1.sort()
    
    s2 = list(s2)
    s2.sort()
    
    s1 = "".join(s1)
    s2 = "".join(s2)
    
    return s1 == s2


s1 = input()
s2 = input()

if solution(s1, s2):
    print("Yes")
else:
    print("No")