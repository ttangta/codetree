class USER:
    def __init__(self, user_id="codetree", user_level=10):
        self.user_id = user_id
        self.user_level = user_level
    def info(self):
        print(f"user {self.user_id} lv {self.user_level}")

user_id, user_level = input().split()

u1 = USER().info()
u2 = USER(user_id, user_level).info()