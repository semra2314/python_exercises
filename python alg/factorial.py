def faktoriyel(n):
    # Taban durum: 0 veya 1 ise sonuç 1'dir.
    if n <= 1:
        return 1
    # Fonksiyon kendini n-1 ile tekrar çağırıyor
    else:
        return n * faktoriyel(n - 1)

print("5 Faktöriyel:", faktoriyel(5)) # 5 * 4 * 3 * 2 * 1 = 120