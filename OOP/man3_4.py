from base_person3_4 import Person, Warrior  # import  * - и тогда импортируются все классы из модуля base_person

man = Person('Hulio', 30, 180)
man.description_person()


warrior = Warrior('Konan', 32, 200)
print(warrior.description_person())

"""Другой вариант"""   # импортируем весь модуль, но тогда при вызове перед классом ставим модуль.
import base_person3_4

man = base_person3_4.Person('Hulio', 30, 180)
man.description_person()