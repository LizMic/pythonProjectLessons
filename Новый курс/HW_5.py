# #Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.

some_str = input("Введите выражение>>")
collect = 0
znak = ''
for element in some_str:
    if element.isdigit():
        if znak == '-':
            collect -= int(element)
        else:
            collect += int(element)
    else:
        znak = element
print(collect)

# #Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

#Вариант 1
some_str = input("Введите выражение>>") + ' '
word = ''
for letter in some_str:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''

#Вариант 2
some_str = input("Введите выражение>>")
print(*some_str.split(),sep='\n')
