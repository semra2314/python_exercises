a=10
b=4
"""
# karşılaştırma operatörleri
print (a==b) # false döner
print (a!=b) # true döner
print (a>b) # true döner
print (a<b) # false
print (a>=b) # true
print (a<=b) #false

# mantıksal operatörler (not,and,or) ile karşılaştırma
print (not a > b) # false döner
print (a<b and a<0) # false döner
print (a<b or a<0) # false döner

# NOT: Python'da boşluklar (indentation) çok önemlidir.

if a>0:
    print ("a pozitiftir")
else:
    print ("a negatif veya sıfırdır")
    
# hatalı örnek
'''
if a > 0:  # Bu satır doğru bir şekilde başlatılmış bir if bloğudur
    print("Pozitif")  # Bu satır da if bloğunun içine girer
    else:  # Bu satır hata verir, çünkü else if bloğunun bir parçası olmalı, ancak yanlış girintilenmiştir.
        print("Negatif veya sıfır")
        
'''
# Yanlış kullanım:
'''
count = 0

while count < 5:  # Bu satır doğru
        print(count)  # Hata: 'print' fonksiyonu yanlış girintilenmiş!

    count += 1  # Hata: 'count' değişkeninin artırılması da yanlış girintilenmiş!
''''''

# Doğru kullanım:
count = 0

while count < 5:
    print(count)
    count += 1
    
# Bazı kullanımlar da yanlış gibi görünebilir ama orijinal olarak doğrudurlar

count = 1
if count == 1:print("Bu doğru bir kullanımdır")

# Python, eğer if bloğu sadece tek bir satırdan (tek bir komuttan) 
# oluşuyorsa, o komutu iki nokta üst üste (:) işaretinden hemen 
# sonra aynı satıra yazmana izin verir.

"""


# Python'da normalde satır sonuna bir şey koymayız.
# Ancak bir satıra birden fazla komut sığdırmak istersen 
# araya ; (Semicolon / Noktalı Virgül) koyabilirsin.

toplam = 0
liste = [1,2,3,4,5,6,7,8,9]
for i in liste: print(i); print("doğru kullanım örneği"); toplam += i
print(toplam)# çıktı:
'''
1
doğru kullanım örneği
2
doğru kullanım örneği
3
doğru kullanım örneği
4
doğru kullanım örneği
5
doğru kullanım örneği
6
doğru kullanım örneği
7
doğru kullanım örneği
8
doğru kullanım örneği
9
doğru kullanım örneği
45
'''


"""
def function():...
function()

burda bir ellips örneği var 
burayı sonra dolduracağım demek
burası boş kalsın ama hata verme demek
önceden 'pass' kelimesi kullanılırmış
"""