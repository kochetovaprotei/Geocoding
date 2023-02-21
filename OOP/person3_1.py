class Person():
    '''''''Класс - Модель человека'''''''
    def __init__(self, name, age):  # метод init
        ''''' Инициализация атрибутов человека - имя, возраст'''
        self.name = name  # атрибут имени
        self.age = age  # атрибут возраста
        print('Man created')

    def sing(self):
        ''''Просим человека спеть'''
        print(self.name + ' is singing')

    def dance(self):
        ''''Просим человека станцевать'''
        print(self.name + ' is dancing')


man = Person('Ksu', 28)
man_not_woman = Person('Alex', 30)
print(man.name)
print(man.age)

man.sing()
man.dance()

man_not_woman.dance()
man.dance()