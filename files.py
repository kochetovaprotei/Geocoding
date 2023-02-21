# fw = open('for_files/file.txt', 'a')   # создать файл и выполняет действие a, права на запись
# fw.write('Hello, world\n')  #записать строку с переносом строки
# fw.close()

# var = input('Write something: ')
# fw = open('for_files/file.txt', 'a')   # создать файл и выполняет действие a, права на запись
# fw.write(var)  #записать строку с переменной
# fw.close()


#a - запись новых данных в файл и помещение новых данных в конец файла
#w - запись новых данных, но с удалением старых данных
#r - чтение данных


# fw = open('for_files/file2.txt', 'w')
# fw.write('hey yo')  #записать строку с переменной
# fw.close()

fr = open('for_files/file2.txt', 'r')
text = fr.read()
fr.close()

print(text)