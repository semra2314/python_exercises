# misal 75 kuruş para üstü verirken; önce en büyük olan 50 kuruşu, sonra kalan 25 kuruşu verirsin
def para_ustu(miktar):
    bozuk_paralar = [200, 100, 50, 25, 10, 5, 1] # TL ler
    sonuc = []
    
    for para in bozuk_paralar:
        while miktar >= para:
            miktar -= para
            sonuc.append(para)
            
    return sonuc

print("Para Üstü Dağılımı:", para_ustu(87)) # Çıktı: [50, 25, 10, 1, 1]