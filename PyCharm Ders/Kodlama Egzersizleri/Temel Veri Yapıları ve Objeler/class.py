
class Hayvan():
    def __init__(self,tür,ayak,renk):
        self.tür=tür
        self.ayak=ayak
        self.renk=renk

class Köpek(Hayvan):
    def __init__(self,tür,ayak,renk,cins):
        super().__init__(tür,ayak,renk)
        self.cins=cins
    def bagır(self):
        print("Hav Hav!")

class Kuş(Hayvan):
    def __init__(self,tür,ayak,renk,cins):
        super().__init__(tür,ayak,renk)
        self.cins=cins
    def bagır(self):
        print("Cik Cik!")

class At(Hayvan):
    def __init__(self,tür,ayak,renk,cins):
        super().__init__(tür,ayak,renk)
        self.cins=cins
    def bagır(self):
        print("İnnnhaaa!")



hayvan = Hayvan("At",4,"Beyaz")
at = At("At",4,"siyah","deli")
kuş = Kuş("Kuş",2,"sarı","muhabbet")
köpek = Köpek("Köpek",4,"gri","pitbull")

köpek.bagır()
kuş.bagır()
at.bagır()
print(at.renk)
print(hayvan.renk)