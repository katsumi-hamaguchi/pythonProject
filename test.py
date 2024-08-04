a = 1234567
b = ["a","b","c"]

print(b[2])

for x,p in enumerate(b):
 print(x)
 print(p)
 p

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


c = [10,20,30]
d = []

d = [i+10*100 for i in c]
print(d)





