c=int(input("Ввведите количество секунд - "))
hh=c//3600
mm=(c%3600)//60
ss=(c%3600)%60

print("{:>02}:{:>02}:{:>02}".format(hh, mm, ss))
