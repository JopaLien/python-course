def pifagor():
    if c == 0 and a != 0 and b != 0:
        print("гипотенуза равна",(a**2+b**2)**0.5)
    if c != 0 and (b == 0 and a == 0):
        print("не хватает данных")
    elif a == 0 and c != 0 or b == 0 and c != 0:
        print("нужный вам катет равен", (c**2-a**2)**0.5 if b == 0  else (c**2-b**2)**0.5)
    elif a != 0 and b != 0 and c != 0:
        print("у вас уже всё есть")
    else:
        print("не хватает данных")

def pinus():
    if a != 0 and c != 0:
        print(a/c)
    else:
        print("не хватает данных")
def copis():
    if b != 0 and c != 0:
        print(b/c)
    else:
        print("не хватает данных")

print("введите значение гипотенузы(если её нет напишите 0)")
c = int(input())
print("введите катет противолежащий(если нет введите 0 )")
a = int(input())
print("введите катет прилежащий(если нет введите 0 )")
b = int(input())
print("какая операция вам нужна?","(1)найти неизвестную сторону","(2)найти синус","(3)найти косинус", sep="\n")
n = int(input())
if n == 1:
    pifagor()
if n == 2:
    pinus()
if n == 3:
    copis()


