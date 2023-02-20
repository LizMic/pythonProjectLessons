a=input("Введите результат пробежки в 1 день в км - ")
b=input("Введите цель километража в день - ")

while True:
    if a.isdigit():
        a=int(a)
        break
    else:
        ("Введенный показатель не соотвествует критериям")
while True:
    if b.isdigit():
        b=int(b)
        break
    else:
        ("Введенный показатель не соотвествует критериям")


day = 1
tmp = a
while tmp <= b:
    tmp *= 1.1
    day += 1

print(day)
print("")
print("Ежедневный результат:")

while a < b:
    print(a)
    a=a+0.1*a
else:
    print(a)