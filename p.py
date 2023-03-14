""""
v = 0
a = int(input())
for i in range(a):
    b=int(input())
    if b % 3 == 0 and b % 10 == 4:
        v+=b
print(v)
"""
""""
a=int(input())
g=0
while a != 0 :   
    if a % 5 == 0 or a % 9 == 0:
        g+=1
    a=int(input())
print(g)
"""
""""
a=int(input())
g=0
for i in range (a):
    f=int(input())
    if f % 3 == 0 and f % 10 == 2:
        g+=1
print(g)
"""
"""
a=int(input())
g = 0
while a != 0:
    if a % 6 == 0 and a % 10 == 4:
        g+=a
    a= int(input())
print(g)
"""
"""
a=[(1,2),(11,2),(1,12),(11,12),(-11,-12),(-11,12),(-12,11),(10,10),(10,5)]
A=11
for i in a:
    s,t = i
    
    if s > 10 or t > A:
        print("ДА")
    else:
        print("НЕТ")
s=2
t=5
s,t=t,s
print(s,t)

s=2
t=5
vedro=s
s=t
t=vedro
print(s,t)
"""

    

