import os # operating system i içe aktar
import subprocess # pythonun terminale erişimi
base_dir = os.path.dirname(os.path.abspath(__file__)) #programın hangi klasörde çalıştığını bulması için
''' 
base_dir : temel dizin ,içine konum bilgisi koyduğumuz değişken ismi
__file__ : "Şu an çalışan bu dosya" demektir.
os.path.abspath : Dosyanın bilgisayardaki tam adresini bulur
os.path.dirname : dosyanın kendisini değil ,içinde bulunduğu klasörü bulur

'''
for folder in os.listdir(base_dir): # Klasörün içindeki her bir dosyaya/klasöre bak
    folder_path = os.path.join(base_dir, folder)
    # os.path.join (yol birleştir): Klasör adresiyle dosya adını güvenli bir şekilde birleştirir.
    
    requirements_path = os.path.join(folder_path, "requirements.txt") 
    if os.path.isdir(folder_path) and os.path.isfile(requirements_path):
        # os.path.isdir: "Bu bir klasör mü?"
        # os.path.isfile: "Bu bir dosya mı?"
        print(f" Kütüphaneler yükleniyor: {requirements_path}")
        subprocess.run(["pip","install","-r",requirements_path],check=True)
        
print("Kütüphaneler yüklendi")