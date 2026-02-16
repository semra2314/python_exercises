def kabarcik_siralama(liste):
    n = len(liste)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if liste[j] > liste[j+1]:
                # Yer değiştirme (Swap) işlemi
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste  #büyük olan en sağa kaydırılarak ve ardından da solda kalan sayılardaki en büyük olanı tekrar sağa kaydırılarak küçükten büyüğe listeyi sıralar

sayilar = [64, 34, 25, 12, 22]
print("Sıralı Liste:", kabarcik_siralama(sayilar))