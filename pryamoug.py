def pifagor(a=None, b=None, c=None):
    if not c:
        print("определение гипотенузы:")
        return gipotenus_find(a, b)
    elif not (a and b):
        print("finding missing catet")
        return catet_find(c, a, b)
    else:
        print("not enough data or everything is defined")

def gipotenus_find(a=None, b=None):
    if a and b:
        c = (int(a)**2+int(b)**2)**0.5
        return c
    else:
        print("not enough data")

def catet_find(c, a=None, b=None):
    if a:
        print("Determening catet b")
        return calculate_catet(a, c)
    else:
        print("Determening catet a")
        return calculate_catet(b, c) 

def calculate_catet(known_catet, c):
    unknown_catet = (int(c) ** 2 - int(known_catet) ** 2) ** 0.5
    return unknown_catet

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
c = input()
print("введите катет противолежащий(если нет введите 0 )")
a = input()
print("введите катет прилежащий(если нет введите 0 )")
b = input()
print("какая операция вам нужна?","(1)найти неизвестную сторону","(2)найти синус","(3)найти косинус", sep="\n")
n = int(input())
if n == 1:
    print(pifagor(a, b, c))
if n == 2:
    pinus()
if n == 3:
    copis()


