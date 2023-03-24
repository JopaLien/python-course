import random
import time

def choice():
    print("Вы выбрали цыплёнка")
l = s = v = 0


def parameter_change(l, s, v, l_delta, s_delta, v_delta, end=""):
    l += l_delta
    s += s_delta
    v += v_delta
    print(end)
    return l, s, v


print("выберите цыплёнка"," (1) жёлтый(10 выносливость,3 скорость)"," (2) чёрный(3 выносливость,3 скорость,3 удача)"," (3) белый(3 выносливость,10 скорость)",sep="\n")

a=input()

decision = "Вы выбрали цыплёнка"

if a == "1":
    l, s, v = parameter_change(0, 10, 3, decision)
elif a == "2":
    l, s, v = parameter_change(3, 3, 3, decision)
elif a == "3":
    l, s, v = parameter_change(0, 10, 3, decision)
print(l, s, v)
# print("Назовите своего цыплёнка")
# n=input()
# if len(n)>=5:
#     l+=1
#     print("говорят,что это имя приносит удачу")
#     time.sleep(1)
# elif len(n)<5 and len(n)!=0:
#     print("Хорошее имя")
#     time.sleep(1)
# elif len(n)==0:
#     l-=2
#     print("это не к добру")
#     time.sleep(1)
# print("Какую провести тренировку?"," (1) на выносливость +5(-1удача)"," (2) на скорость +5(-1удача)"," (3) она нам не нужна(+1удача)",sep="\n")
# b=input()
# if b == "1":
#     v+=5
#     l-=1
#     print("Хорошая тренировка!")
#     time.sleep(1)
# elif b == "3":
#     l+=1
#     print("это ваш выбор")
#     time.sleep(1)
# elif b== "2":
#     s+=3
#     l-=1
#     print("Хорошая тренировка!")
#     time.sleep(1)
# print("Пора отправляться на гонку!")
# u=random.randint(1,10)
# if u>=3:
#     print("какой-то доктор предлагает лекарства для улучшения выносливости вашего цыплёнка","взять таблетки?(да/нет)",sep="\n")
#     o=input()
#     if o == "нет":
#         l+=1
#         print("Вот вы и прибыли на турнир")
#         time.sleep(2)
#     if o == "да":
#         o=random.randint(1,10)
#         if o<5:
#             print("ваш цыплёнок умер из-за таблеток")
#             exit()
#         v+=3
#         print("ваш цыплёнок выглядит сильнее")
#         print("Вот вы и прибыли на турнир")
#         time.sleep(2)
# print("Выберите дистанцию(5,10,15)")
# y=int(input())
# print("Гонка начнётся через...")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# print("Марш!!")
# for i in range(4):
#     print("ваш цыплёнок бежит")
#     time.sleep(1)
# if l>=5:
#     print("ваш цыпленок",n,"нашёл короткий путь и","занял первое место")
#     exit()
# x=(v-y)
# if s>=y and x>0:
#     q=random.randint(1,10)
#     if q>6:
#         print("ваш цыпленок",n,"занял первое место ")
#     else:
#         print("ваш цыпленок",n,"занял второе место")
# if s<y and x>0:
#     print("ваш цыплёнок",n,"занял последнее место")
# if v<y:
#     print("вашему цыплёнку не хватило сил, чтобы добежать до финиша")
# 
#     
