def asal_mi(sayi):
    if sayi <= 1:
        return False
    # Sayının kareköküne kadar bölünür mü diye bakarız (Performans için)
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Kullanım
sayi = int(input("Bir sayı girin: "))
if asal_mi(sayi):
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")