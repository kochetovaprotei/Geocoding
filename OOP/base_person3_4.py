class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + " " + str(self.age) + " years old " + str(self.height) + "cm " + str(self.weight) + "kg "
        print("New person is " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("His weight is " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение ярости человека"""
        print("His rage is " + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + " " + str(self.age) + " years old " + str(self.rage)
        # print("New person is " + description)
        return description

# man = Person('Hulio', 30, 180)
# man.description_person()

# warrior = Warrior('Konan', 32, 200)
# print(warrior.description_person())