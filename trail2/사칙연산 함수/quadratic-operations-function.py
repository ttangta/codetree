def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def div(a, c):
    return a // c

def mul(a, c):
    return a * c

def solution(a, o, c):
    answer = None
    if o == "+":
        answer = plus(a, c)
    elif o == "-":
        answer = minus(a, c)
    elif o == "/":
        answer =  div(a, c)
    elif o == "*":
        answer = mul(a, c)
    if answer == None: return False
    return f"{a} {o} {c} = {answer}"

a, o, c = input().split()

a = int(a)
c = int(c)

print(solution(a, o, c))