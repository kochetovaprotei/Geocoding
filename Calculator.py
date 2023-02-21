first_number = int(input('Enter first number: '))
action = input('Enter "+" or "/" or "*" or "-": ')
second_number = int(input('Enter second number: '))
sub = '-'
add = '+'
mul = '*'
div = '/'


def subtraction():
    result_subtraction = first_number - second_number
    return result_subtraction


b = subtraction()


def addition():
    result_addition = first_number + second_number
    return result_addition


a = addition()


def multiplication():
    result_multiplication = first_number * second_number
    return result_multiplication


d = multiplication()


def division():
    if second_number > 0:
        result_division = first_number / second_number
        return int(result_division)
    else:
        result_division = 0
        print('You can not divide to 0. Result = ' + str(result_division))


c = division()


if action == add:
    print(a)
elif action == sub:
    print(b)
elif action == div:
    print(c)
elif action == mul:
    print(d)
else:
    print('Start again')
