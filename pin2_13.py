pin = 1234
print('Please, enter code:')
user_pin = int(input())

if pin == user_pin:
    print('Какую сумму вы хотите снять')
else:
    print('Error, try again, you have 2 tries')
    print('Please, enter code')
    user_pin = int(input())
    if pin == user_pin:
        print('Какую сумму вы хотите снять')
    else:
        print('Error, try again, you have 1 try')
        print('Please, enter code')
        user_pin = int(input())
        if pin == user_pin:
            print('Какую сумму вы хотите снять')
        else:
            print('Sorry, card is blocked. Please, turn to your bank')