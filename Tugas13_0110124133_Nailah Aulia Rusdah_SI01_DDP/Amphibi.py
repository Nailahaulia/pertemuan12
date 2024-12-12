from Animal import Animal

class Amphibi(Animal):
    def __init__(self, nama,makanan,hidup,berkembang_biak,jenis_air,bernapas):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_Amphibi(self):
        super().info_animal(),
        print(f"Jenis air \t\t\t :" ,self.jenis_air, "\nbernafas\t\t\t :", self.bernapas)


#manggilnya nama objeknya bukan nama classnya
amphibi = Amphibi("kadal air","serangga","dua alam","bertelur", "air tawar","kulit dan paru paru")
amphibi.info_Amphibi()
amphibi = Amphibi("axolotl","cacing dan ikan kecil","air","bertelur","air tawar","insang dan paru-paru")
amphibi.info_Amphibi()
amphibi = Amphibi("sesilia","serangga dan rayap","dalam tanah","bertelur dan melahirkan","air tawar","kulit")
amphibi.info_Amphibi()