def solution(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 !=0:
            return False
        return True
    return False

if solution(int(input())):
    print("true")
else:
    print("false")