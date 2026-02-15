# Temel veri tipleri

x=5 #integer
y=3.14 #float
name="semra" #string
is_student=True #boolean
items=[1,2,3] #list
diction = {"isim" : "Semra"}#dictionary

print(type(x)) # çıktı : <class 'int'>
print(type(y)) # çıktı : <class 'float'>
print(type(name)) # çıktı : <class 'str'>
print(type(is_student)) # çıktı : <class 'bool'>
print(type(items)) # çıktı : <class 'list'>
print(type(diction)) # çıktı : <class 'dict'>

# şimdi bunun farklı versiyonunu yapalım
print (type(x) == int) # çıktı : True
print (type(y) == float) # çıktı : true
print (type(name) == str)
print (type(is_student) == bool)
print (type(items) == list)
print (type(diction) == dict)

# başka sınıflara dönüştürme

print(float(x)) # çıktı : 5.0
print(int(y)) # çıktı : 3
print(str(is_student)) # çıktı : True
print(list(name)) # çıktı : ['s', 'e', 'm', 'r', 'a']
print(dict(surname="kaya")) # çıktı : {'surname': 'kaya'}

print(int("80"),float("80"), "80" ,list("80"))
# çıktı:80 80.0 80 ['8', '0']
