def solution(n):
    sum_n = int(str(n)[0]) + int(str(n)[1])
    return n%2 == 0 and sum_n % 5 == 0


n = int(input())
if solution(n):
    print("Yes")
else:
    print("No")