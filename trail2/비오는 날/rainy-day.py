# 윤년 판단하는 함수
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400 == 0:
                return True
            else: return False
        else:return True
    return False

# 각 인덱스 번호가 month
DAYS = [0, 31, (28,29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 유효한 날짜인지 판단하는 함수
def is_valid_date(date):
    year, month, day = map(int, date.split("-"))
    limit_day = None

    # 문제에서 유효한 year이 아니면 False 반환
    if year < 2000 or year > 2100:
        return False
    # 유효한 month가 아니면 False 반환
    elif month < 1 or month > 12:
        return False

    # 만약 2월달이면 윤년인지 판단해서 limit_day를 갱신
    if month == 2:
        if is_leap_year(year):
            limit_day = DAYS[month][1]
        else:
            limit_day = DAYS[month][0]
    else:
        limit_day = DAYS[month]

    return 1 <= day <= limit_day

class Data:
    def __init__(self, date, week, weather):
        self.date = date
        self.week = week
        self.weather = weather
        self.information = list(map(int, date.split("-")))

    def info(self):
        print(f"{self.date} {self.week} {self.weather}")

def solution(arr):
    answer = arr.copy()
    answer.sort(key=lambda x:x.information)

    return answer

n = int(input())

arr = []
for _ in range(n):
    s = input().split()
    if is_valid_date(s[0]) and s[2] == "Rain":
        arr.append(Data(s[0], s[1], s[2]))

answer = solution(arr)
answer[0].info()