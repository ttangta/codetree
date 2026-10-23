a, b = ord("a"), ord("z")
S = (b - a) + 1

COUNT = [0] * S

def solution(A):
    for s in A:
        COUNT[ord("a") - ord(s)] += 1

    cnt = 0
    for c in COUNT:
        if c > 0: cnt +=1

    return not cnt <= 1

A = input()
if solution(A):
    print("Yes")
else:
    print("No")