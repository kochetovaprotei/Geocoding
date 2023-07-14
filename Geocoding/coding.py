def add(a, b):
    return  a + b

print(add(4, 8))

x = 19
y = 23
s = add(x, y)
print(s)  # 42

def say_hello():
    print("Hello!")

say_hello()


# """В переменную word введите слово.
# В переменную n введите индекс символа.
# Напечатайте символ с этим индексом, если такой индекс есть в слове.
# Иначе напечатайте Index is not valid."""
#
# word = input("Enter word: ")
# n = int(input("Enter index:"))
# if n in word:
#     print(word[n])
# else:
#     print("Index is not valid")

# """В переменную char введите символ. Определите, является ли этот символ гласной буквой."""
#
# char = input("Enter simbol: ")
# if char in "aoieu":
#     print("vowel")
# else:
#     print("No")
#
# """В переменную name введите имя. Определите, начинается ли имя с гласной буквы."""
#
# name = input("Enter name: ")
# if name[0] in "aoieu":
#     print(name[0])
# else:
#     print("Failed")

# """В переменную string введите строку. Определите, является ли последний символ строки цифрой от 0 до 9."""
#
# string = input("Enter name: ")
# if name[0] in "aoieu":
#     print(name[0])
# else:
#     print("Failed")

# """6. С помощью команды input в переменную answer введите ответ пользователя на вопрос: "Are you ok?".
# Если ответ "No" или "no", напечатайте "Get better!". В противном случае напечатайте "Cool!"""
#
# answer = input("Are you ok? \n- ")
# if answer == "No":
#     print("Get better!")
# elif answer == "no":
#     print("Get better!")
# else:
#     print("Cool!")
