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

man = Person('Hulio', 30, 180)

man.update_weight(90)
man.get_weight()