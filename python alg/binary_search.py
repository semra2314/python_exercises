def ikili_arama(liste, hedef):
    dusuk = 0
    yuksek = len(liste) - 1
    
    while dusuk <= yuksek:
        orta = (dusuk + yuksek) // 2 # Middle point
        if liste[orta] == hedef:
            return orta # Hedef bulundu
        elif liste[orta] < hedef:
            dusuk = orta + 1 # Sağ tarafa bak
        else:
            yuksek = orta - 1 # Sol tarafa bak
            
    return -1 # Bulunamadı

liste = [10, 20, 30, 40, 50]
print("Elemanın indeksi:", ikili_arama(liste, 40))

# Listeyi her seferinde ortadan ikiye bölerek arama alanını daraltır.
# ağaç yapısı gibi düşünürseniz daha kolay anlaşılıyor

# O(log n): Binary Search çok hızlıdır;
# liste boyutu milyon kat artsa bile işlem sayısı sadece çok küçük bir miktar artar.