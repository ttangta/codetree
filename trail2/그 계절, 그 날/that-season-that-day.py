DAYS = [0, 31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_yoon(y):
    return y % 4 == 0 and (y % 100 != 0) or (y% 100 == 0 and y % 400 == 0)

def is_exists(m, d):
    return 1 <= d <= DAYS[m]

def solution(y, m, d):
    # 윤년일 때 2월달의 마지막 일자 결정
    if is_yoon(y):
        DAYS[2] = DAYS[2][1]
    else:
        DAYS[2] = DAYS[2][0]



    # 입력받은 m에 해당하는 d가 유효한지 체크
    if m <=0 or m >= 13: return -1
    if not is_exists(m, d): return -1

    if 3 <= m <= 5: return "Spring"
    elif 6 <= m <= 8: return "Summer"
    elif 9 <= m <= 11: return "Fall"
    elif m == 12 or 1 <= m <= 2: return "Winter"

y, m, d = map(int, input().split())

print(solution(y, m, d))