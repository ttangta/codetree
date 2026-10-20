S, Q = input().split()
Q = int(Q)


for _ in range(Q):
    S = list(S)
    q, t1, t2 = input().split()
    
    # 입력받은 q를 먼저 정수로 변환 후 어떤 종류의 질의인지에 따라 분기
    q = int(q)
    
    # q가 1일 때 t1번 문자와  t2번 문자 교환
    if q == 1:
        t1, t2 = int(t1)-1, int(t2)-1
        S[t1], S[t2] = S[t2], S[t1]
        
    # q가 2일 때 t1 문자 전부 t2로 교환
    elif q == 2:
        for i in range(len(S)):
            if S[i] == t1:
                S[i] = t2
    
    print("".join(S))