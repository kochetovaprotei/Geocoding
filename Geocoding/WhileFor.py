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


"""Реализуйте функцию-предикат is_arguments_for_substr_correct(), которая принимает три аргумента:

    строку;
    индекс, с которого начинать извлечение;
    длину извлекаемой подстроки.

Функция возвращает False, если хотя бы одно из условий истинно:

    Отрицательная длина извлекаемой подстроки.
    Отрицательный заданный индекс.
    Заданный индекс выходит за границу всей строки.
    Длина подстроки в сумме с заданным индексом выходит за границу всей строки.

В ином случае функция возвращает True."""
def is_arguments_for_substr_correct(string, start_index, length_substr):
    if length_substr < 0:
        return False
    elif start_index < 0:
        return False
    elif start_index > len(string) - 1:
        return False
    elif (length_substr + start_index) > len(string):
        return False
    else:
        return True


"""Реализуйте функцию filter_string(), принимающую на вход строку и символ, и возвращающую новую строку, в которой 
удален переданный символ во всех его позициях."""

def filter_string(string, symbol):
    i = 0
    result = ""
    while i < len(string):
        if string[i] != symbol:
            result = result + string[i]
        i = i + 1
    return result

# text = 'If I look back I am lost'
# filter_string(text, 'I')  # 'f  look back  am lost'

"""Рассмотрим алгоритм проверки простоты числа. Будем делить искомое число x на все числа из диапазона 
от двух до x - 1 и смотреть остаток. Если в этом диапазоне не найден делитель, который делит число x без остатка,
 значит, перед нами простое число."""

def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True

print(is_prime(1))  # => False


"""Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, содержит ли строка указанную букву"""

def is_contains_char(string, letter):
    i = 0
    while i < len(string):
        if string[i] == letter:
            return True
        i = i + 1
    return False

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False



"""Посмотрим, как реализовать функцию переворота строки через цикл for:"""

# text - произвольный текст
# char - символ, который нужно учитывать
def chars_count(text, char):
    # Так как ищем сумму, то начальное значение 0
    result = 0
    for current_char in text:
        # приводим все к нижнему регистру,
        # чтобы не зависеть от текущего регистра
        if current_char.lower() == char.lower():
            result += 1
    return result


chars_count('hexlet!', 'e')  # 2
chars_count('hExlet!', 'e')  # 2


"""принимает на вход строку и символ и возвращает новую строку, в которой удалён 
переданный символ во всех его позициях. """

def filter_string(string, symbol):
    # Начальное значение
    result = ''
    for current_symbol in string:
        if current_symbol.lower() != symbol.lower():
            result = result + current_symbol
    return result

text = 'If I look forward I win'
filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win'