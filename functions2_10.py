def summ():

    print('hello')

summ()


num_1 = 10
num_2 = 20

def summ():
    result = num_1 + num_2
    print(result)


summ()


def summ(num_3, num_4):
    result = num_3 + num_4
    print(result)


summ(10, 20)
summ(30, 40)

def greetings(name):
    print('Hello ' + name)

greetings('ks')


def greetings(name='ks'):
    print('Hello ' + name)

greetings()


name = 'ks'
def greetings(name):
    print('Hello ' + name)

greetings(name)


def greetings(myname, age):
    print('Hello, my name is ' + myname + ', I"m ' + age + ' years old')


greetings('Ks', '28')


myname1 = input()
age1 = input()
def greetings(myname1, age1):
    print('Hello, my name is ' + myname1 + ', I"m ' + age1 + ' years old')


greetings(myname1, age1)


name2 = 'Ksu'
age2 = '28'
def greetings(name2, age2):
    result = name2 + ' ' + age2
    return(result)

a = greetings(name2, age2)
print(a)

# либо аналог

name3 = 'Ksu'
age3 = '28'
def greetings(name3, age3):
    result = name3 + ' ' + age3
    print(result)
    # return(result)

# a = greetings(name2, age2)
greetings(name3, age3)