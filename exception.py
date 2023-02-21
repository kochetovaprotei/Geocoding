a = int(input('Write first value: '))
b = int(input('Write second value: '))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print('You can not divide to 0')
print('Result : ' + str(result))

result_2 = a + b
print('Result_2 ' + str(result_2))


