def solution(s):
    s = list(s)
    s.sort()
    return  "".join(s)

s = input()

print(solution(s))