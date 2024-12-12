from Animal import Animal

class Mamalia (Animal):
    def __init__(self, nama,makanan,hidup,berkembang_biak,jenis_kulit,ukuran_tubuh):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh

    def info_Mamalia(self):
        super().info_animal()
        print("Jenis kulit\t\t\t :",self.jenis_kulit , "\nUkuran tubuh \t\t\t:", self.ukuran_tubuh)

    def suara(self):
        return f"{self.nama} mengeluarkan suara lucu"


gajah = Mamalia("Gajah","Tumbuh-tumbuhan","Darat","Melahirkan","Sedikit Berbulu","Sangat besar")
gajah.info_Mamalia()
print()
print(gajah.suara())
print()

kucing = Mamalia("Kucing","Daging","Darat","Melahirkan","Berbulu","Kecil ")
kucing.info_Mamalia()
print()
print(kucing.suara())

lumba_lumba = Mamalia("Lumba-lumba","Daging","Air","Melahirkan","tidak berbulu","sedang")
lumba_lumba.info_Mamalia()
print()
print(lumba_lumba.suara())