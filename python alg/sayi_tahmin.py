import random

def sayi_tahmin():
    hedef = random.randint(1, 100) # 1 ile 100 arası rastgele sayı
    deneme_sayisi = 0
    
    while True:
        tahmin = int(input(" Guess a number: "))
        deneme_sayisi += 1
        
        if tahmin < hedef:
            print("Higher")
        elif tahmin > hedef:
            print("Lower")
        else:
            print(f"Tebrikler! {deneme_sayisi} denemede buldun.")
            break

