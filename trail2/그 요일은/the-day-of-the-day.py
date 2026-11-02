DAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DayOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def days_sum(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += DAYS[i]
    total_days += d

    return total_days

def solution(s1, s2, target):
    gap = s2 - s1
    start_point = 0
    answer = 0
    for i, v  in enumerate(DayOfWeek):
        if target == v:
            start_point += i
            answer += 1
            break
    gap -= start_point
    answer += gap // 7
    return answer

m1, d1, m2, d2 = map(int, input().split())
target = input()

s1 = days_sum(m1, d1)
s2 = days_sum(m2, d2)
print(solution(s1, s2, target))
