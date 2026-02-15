# string manipülasyonları
string = "     öRnEk StRiNg     "

string = string.upper()     #tüm harfleri büyük yaptı
print(string) #çıktı :"     ÖRNEK STRING     "

string = string.lower()     #tüm harfleri küçük yaptı
print(string) #çıktı :"     örnek string     "

string = string.title()     #ilk harfleri büyük yaptı
print(string) #çıktı :"     Örnek String     "

string = string.strip()     #baştaki ve sondaki boşlukları kaldırdı ***********************************
print(string) #çıktı :"Örnek String"

string = string.lstrip()    #soldaki boşlukları kaldırdı
print(string) #çıktı :"Örnek String     "

string = string.rstrip()    #sağdaki boşlukları kaldırdı
print(string) #çıktı :"     Örnek String"

string = string.capitalize()    #ilk harfi büyük yapar diğerleri küçük tutulur
print(string) #çıktı :"Örnek string"

string = string.replace("string", "yazı")   #kelimeyi değiştirdi
print(string) #çıktı :"Örnek yazı"

string += "text"
print(string) #çıktı :"Örnek yazıtext"

string = "baş" + string
print(string) #çıktı :"başÖrnek yazıtext"

print(len(string)) #string uzunluğu =17

# PRİNT FORMATLARI

# fonk la yazdırma
print ("fonk la yazdırma:", string)

# formatlayarak yazdırma                            *****************
print (f"formatlanan yazı : {string}")

# formatlamaya alternatif                           *****************
print ("formatlanan yazı2 : {}".format(string))

# ekleme yaparak yazdırma
print("ekleyerek yazdırma:" + string)
