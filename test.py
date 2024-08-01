a = 123

print(f"baa {a}")

class Test :
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name}aaaaa")


katsumi = Test("katsumi",29)
print(katsumi.name)
print(katsumi.age)
katsumi.run()




