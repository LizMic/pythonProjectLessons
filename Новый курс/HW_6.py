# #30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент>>"))
n = int(input("Введите количество элементов>>"))
d = int(input("Введите шаг>>"))
an = a+(n-1)*d
print("Итоговый элемент =", an)
for i in range(n):
    print("Значение:", a + i * d)

# #32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

N = int(input("Ввведите количество элементов>"))
pul = list()
for i in range(N):
    list_1 = int(input("Введите элемент массива>>"))
    pul.append(list_1)
print(pul)
min_number = int(input("Введите минимальное значение>>"))
max_number = int(input("Введите максимальное значение>>"))
for i in range(len(pul)):
    if min_number <= pul[i] <= max_number:
        print(i)
