str_1 = 'hello'
print(str_1)
print('hello')

str_1 = 5
str_2 = 10
result = str_1 + str_2
print('Result : ' + str(result))
print('Result : ' + str(15))


str_1 = 'hello'
str_2 = 'WORLD'
print(str_1)
print(dir(str_1))  # покажет функции, которые можно выполнить с этой переменной
print(str_1.upper())  # переведет все символы в верхний регистр
print(str_1.title())  # переведет первый символ в верхний регистр
print(str_2)
print(str_2.lower())


name = 'Ivan'
a = 'Hello {}'  # область куда можно подставить какое-то значение типа строчных данных
print(a.format(name))  # включает в себя нужную переменную


first_name = 'Ivan'
last_name = 'Ivanov'
a = '{} {}'
result = a.format(first_name, last_name)
print('My name is ' + result)

# или аналог

result = f'{first_name} {last_name}'
print('My name is ' + result)