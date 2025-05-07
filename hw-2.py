class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет действие")

    def attack(self):
        print(f"{self.name} атакует")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 50:
                print(f"{self.name} успешно атакует оставшиеся стрелы: {self.arrows}")
            else:
                print(f"{self.name} неудачно атакует оставшиеся стрелы: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и восстанавливает стрелы текущий запас стрел: {self.arrows}")

    def status(self):
        return f"имя: {self.name}, здоровье: {self.hp}, стрелы: {self.arrows}, точность: {self.precision}"



archer1 = Archer("Лука", 100, 10, 75)


archer1.action()
archer1.attack()
archer1.rest()
archer1.attack()
print(archer1.status())
