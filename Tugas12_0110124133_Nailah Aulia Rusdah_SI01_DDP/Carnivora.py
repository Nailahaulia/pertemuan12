from Animal import Animal

class Carnivora(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, taring, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.taring = taring
        self.habitat = habitat

    def info_Carnivora(self):
        super().info_animal()
        print("Taring\t\t\t\t :",self.taring , "\nhabitat \t\t\t :", self.habitat)


    def suara(self):
        return f"{self.nama} mengeluarkan suara Ganas"
    
harimau = Carnivora("Harimau","Daging","Darat","melahirkan","tajam","padang rumput")
harimau.info_Carnivora()
print(harimau.suara())
print()
serigala = Carnivora("Serigala","pemakan segalanya","Darat","melahirkan","Kuat","Hutan")
serigala.info_Carnivora()
print(serigala.suara())
print()
ular = Carnivora("Ular","daging","darat","bertelur","yang tajam","rawa-rawa")
ular.info_Carnivora()
print(ular.suara())