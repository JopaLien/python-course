import random

""""
def jopa():
    print("JopaLien")
jopa()
"""
"""""
a=random.randint (1,11)
print(a)
"""""
"""""
a=[1,2,3]
b=int(input())
print(a[b])
"""
a=["","а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
b=input()
v=int(input())
#b="зьзькькьъ" 
#v=5
for i in range(len(b)):
    b=b.replace(b[i],a[(a.index(b[i])+v)%33],1)
print(b)

