N1, N2 = map(int, input().split())

A = list(map(int, input().split()))[:N1]
B = list(map(int, input().split()))[:N2]

# A 배열에서 N2길이만큼 잘라내며 두 배열의 값이 동일한 경우 반복문을 탈출하고 Flag를 True로 변환
flag = False
for i in range(N1-N2+1):
    sub = A[i:i+N2]
    if sub == B:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")