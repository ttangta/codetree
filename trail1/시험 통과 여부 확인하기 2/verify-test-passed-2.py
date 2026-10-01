n = int(input())

students = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for student in students:
    avg = sum(student)/4
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)