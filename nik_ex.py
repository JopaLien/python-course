a=["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
b = input()
b = list(b)
v = int(input())
a_len = len(a)
for i in range(len(b)):
    idx = a.index(b[i])
    b[i] = a[(idx+v) % a_len]  
    
print("".join(b))

