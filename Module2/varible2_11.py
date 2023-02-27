var_1 = 100  # глобальная переменная
var_2 = 20  # глобальная переменная
# print(var_1, var_2)

def total():
    var_1 = 30  # локальная переменная
    var_2 = 40  # локальная переменная
    result = var_1 + var_2
    print(result)
print(var_1, var_2)
total()




def total():
    result = var_1 + var_2
    print(result)


total()


def sub():
    result = var_1 - var_2
    print(result)


sub()