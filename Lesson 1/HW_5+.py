V=int(input("Введите значение выручки за месяц - "))
I=int(input("Введите значение издержек за месяц - "))
if V>I:
    print("Прибыль! Так держать!")
    print("Рентабельность составила >>")
    print((V-I)/V)
    P=int(input("Введите численность сотрудников фирмы - "))
    print("Прибыль фирмы на одного сотрудника составляет >>")
    print((V-I)/P)
else:
    print("Убыток.. Надо постараться!")