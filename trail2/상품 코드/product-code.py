class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

    def info(self):
        print(f"product {self.code} is {self.name}")

name, code = input().split()
code = int(code)

p1 = Product().info()

p2 = Product(name, code).info()