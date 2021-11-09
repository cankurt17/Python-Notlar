class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileriGöster(self):
        print("""
        Yazılımcının özellikleri:

        İsim: {} 
        Maaş: {} 
        Departman: {}

        """.format(self.isim, self.maaş, self.departman))

    def departmanDegistir(self, yeni_departman):
        self.departman = yeni_departman
class Yönetici(Çalışan):
    def __init__(self, isim, maaş, departman, kişi_sayısı):
        super().__init__(isim, maaş, departman)
        print("Yönetici  sınıfının init fonksiyonu")
        self.kişi_sayısı = kişi_sayısı

    def zamYap(self, miktar):
        self.maaş += miktar

    def bilgileriGöster(self):
        print("""
        Yazılımcının özellikleri:

        İsim: {} 
        Maaş: {} 
        Departman: {}
        Sorumlu Kişi Sayısı:{}

        """.format(self.isim, self.maaş, self.departman, self.kişi_sayısı))

yönetici = Yönetici("Cankurt",2,"Bilişim",5)
yönetici.bilgileriGöster()