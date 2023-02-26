print ("налей молоко в стакан объёмом...", end="") # Между принт и скобкой не нужен пробел print( , а остальное нормально
# Предлагаю изменить все int(input()) на float(input()), чтобы пользователь мог вводить дробные числа
a=int(input()) # a = int(input()) - PEP8
# Ты проверяешь, если значение равно нулю, а что если юзер введет значение ниже 0? 
# Предлагаю изменить условие на a <= 0, чтобы учитывать только натуральные числа 
if a==0: # a == 0 - PEP8
    print("ты забыл взять стакан?")
    exit()
print("сколько литров молока ты нальёшь?", end="") # Good
# Необходимо также учесть, что пользователь может ввести негативное значение по аналогии с а, только использовать b < 0, так как при принте есть условие b == 0
b=int(input()) # b = int(input())
# Данный код можно реализовать более рационально, так как при каждом запуске кода проверяются все 4 условия
# Можно использовать элиф, в таком случае он будет проверять последовательно, если какое-то из предыдущих условий выполняется, то элиф не проверяется 
# if a<b:
#     print("ты налил(а) слишком много молока")
# if a>b and b!=0:
#     print("ты налил(а) достаточно молока")
# if a==b:
#     print("пей аккуратно")
# if b==0:
#     print("у тебя нет молока?")
if a < b:
    print("ты налил(а) слишком много молока")
elif a == b:
    print("пей аккуратно")
elif b == 0:
    print("у тебя нет молока?")
else: # Если никакие другие условия не выполнились, тогда a > b and b != 0
    print("ты налил(а) достаточно молока")
