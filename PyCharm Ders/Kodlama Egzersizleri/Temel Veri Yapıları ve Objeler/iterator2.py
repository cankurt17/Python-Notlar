


class Kareler():

    def __init__(self,sayı):
        self.sayı=sayı
        self.hane=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.hane<self.sayı:
            print(self.hane**2)
            self.hane+=1
        else:
            self.hane=1
            raise StopIteration

kare = Kareler(4)

next(kare)
next(kare)
next(kare)
next(kare)
