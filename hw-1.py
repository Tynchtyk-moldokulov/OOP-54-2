class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"привет меня зовут {self.name} мне {self.age} лет мой город {self.city}")

    def is_adult(self):
        return self.age >= 18


p1 = Person("камила", 20, "бишкек")
p2 = Person("айзар", 16, "ош")

p1.introduce()
p2.introduce()

print(p1.is_adult())
print(p2.is_adult())
