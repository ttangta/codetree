class DATA:
    def __init__(self, sc, mp, t):
        self.secret_code = sc
        self.meeting_point = mp
        self.time = t
def solution(d):
    print(f"secret code : {d.secret_code}")
    print(f"meeting point : {d.meeting_point}")
    print(f"time : {d.time}")

sc, mp, t = input().split()
t = int(t)
d = DATA(sc,mp,t)
solution(d)
