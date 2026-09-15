def solution(n):
    cnt1 = cnt2 = cnt3 = 0

    for i in range(1, n+1):
        if i % 12 == 0:
            cnt3 +=1
        elif i % 3 == 0:
            cnt2 +=1
        elif i % 2 == 0:
            cnt1 +=1

    return cnt1, cnt2, cnt3

n = int(input())
r1, r2, r3 = solution(n)
print(r1, r2, r3)