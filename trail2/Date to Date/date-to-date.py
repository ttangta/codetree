def solution(m1, d1, m2, d2):
    start = 0
    for m in range(m1-1):
        start += month_of_day[m]
    start += d1

    end = 0
    for m in range(m2-1):
        end += month_of_day[m]
    end += d2

    return end - start + 1


month_of_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

answer = solution(m1, d1, m2, d2)
print(answer)