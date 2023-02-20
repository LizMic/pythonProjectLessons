
while True:
    c=input("Ввведите целое положительное число - ")
    if c.isdigit():
        c=int(c)
        break
    else:
        print("Заданный показатель не соответствует критериям")

result=0
while c and result !=9:
    b=c%10
    if b > result:
        result=b
    c//=10

print(result)

