def solution(a, b):
    condidate_sum_val = 0

    for i in range(a, b+1):
        if i % 6 == 0 and i % 8 != 0:
            condidate_sum_val += i

    return condidate_sum_val

a, b = map(int,input().split())
print(solution(a, b))