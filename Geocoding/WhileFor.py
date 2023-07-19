"""Цикл While"""
"""функцию print_numbers() так, чтобы она выводила числа в обратном порядке"""


def print_numbers(last_number):
    # i сокращение от index (порядковый номер)
    # используется по общему соглашению во множестве языков
    # как счетчик цикла
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')


print_numbers(4)

"""Агрегация данных (Числа)"""
"""# Реализуем функцию, которая складывает числа в указанном диапазоне, включая границы."""


def sum_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i  # Считаем сумму для каждого числа
        i = i + 1  # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return sum


sum_numbers_from_range(5, 7)  # 5 + 6 + 7 = 18

"""Реализуйте функцию multiply_numbers_from_range(), которая перемножает числа в указанном диапазоне включая границы диапазона."""


def multiply_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    multiply = 1  # Инициализация произведения
    while i <= finish:  # Двигаемся до конца диапазона
        multiply = multiply * i  # Считаем произведение для каждого числа
        i = i + 1  # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return multiply


multiply_numbers_from_range(1, 5)  # 1 * 2 * 3 * 4 * 5 = 120

"""Агрегация данных (Строки)"""
"""функцию, которая умеет умножать строку — повторяет ее указанное количество раз"""


def repeat(text, times):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = 1

    while i <= times:
        # Каждый раз добавляем строку к результату
        result = result + text
        i = i + 1

    return result


repeat('hexlet', 3)  # 'hexlethexlethexlet'

"""Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:"""


def join_numbers_from_range(start, finish):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = start

    while i <= finish:
        # Каждый раз добавляем строку к результату
        result = result + str(i)
        i = i + 1

    return result


"""Обход строк"""
"""пример кода, который печатает буквы каждого слова на отдельной строке"""


def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки,
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1


name = 'Arya'
print_name_by_symbol(name)

"""Реализуйте функцию print_reversed_word_by_symbol(), которая печатает переданное слово посимвольно"""


def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    # Такая проверка будет выполняться до конца строки,
    # включая последний символ. Его индекс `length - 1`.
    while i >= 0:
        # Обращаемся к символу по индексу
        print(word[i])
        i = i - 1


"""Представьте функцию, которая считает, сколько раз входит буква в предложение. Пример ее работы:"""


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count


a = count_chars('Fear cuts deeper than swords.', 'e')
print(a)


def count_chars_all(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char.upper() or string[index] == char.lower():
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count


b = count_chars_all('HexlEt', 'e')  # 2
print(b)

"""Формирование строк в циклах"""

"""Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины"""
def my_substr(string, length):
    i = 0
    result = ''

    while i <= length - 1:
        current_char = string[i]
        result = result + current_char
        i = i + 1

    return result

print(my_substr('If I look back I am lost', 2))


"""Цикл For"""
"""Посмотрим, как реализовать функцию переворота строки через цикл for"""

def reverse_string(text):
    # Начальное значение
    result = ''
    # char - переменная, в которую записывается текущий символ
    for char in text:
        # Соединяем в обратном порядке
        result = char + result
    # Цикл заканчивается, когда пройдена вся строка
    return result


reverse_string('go!')  # => '!og'

