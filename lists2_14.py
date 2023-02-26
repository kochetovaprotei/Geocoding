
stuff = ['Ksu', 'Alex', 'Ivan']
# print(stuff[0])
#
#
#
# result = stuff[0] + ' ' + stuff[2]
# print(result + ' best result')
number = [1, 15, 23, 4]
# print(number[2])
#
# result_num = number[0] + number[1]
# print(result_num)


print(len(stuff))       # длина списка
print(stuff[-1])    # вывод последнего звена
print(stuff[0:2])   # вывод звеньев 0 и 1
print(stuff[1:])    # вывод с 1 и до конца

stuff.append('Fedor')
print(stuff)

pn = []
pn.append(stuff)
pn.append(number)
print(pn)