DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DayOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
def solution(m1, d1, m2, d2):
    answer = None
    idx = None
    # 만약 같은 달이라면
    if m1 == m2:
        idx = (d2-d1)
    else:
        if m1 < m2:
            idx = DAYS[m1] - d1
            for i in range(m1+1, m2):
                idx += DAYS[i]
            idx += d2
        else:
            idx = d1
            for i in range(m1-1, m2, -1):
                idx += DAYS[i]
            idx += DAYS[m2] - d2
            idx *= -1
    idx %= 7
    return DayOfWeek[idx]
m1, d1, m2, d2 = map(int, input().split())

print(solution(m1, d1, m2, d2))