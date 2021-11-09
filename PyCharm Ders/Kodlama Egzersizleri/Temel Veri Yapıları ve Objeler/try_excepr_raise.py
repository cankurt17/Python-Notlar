

liste= [3,4,5,6,7,8,9,10]

def kontrol(sayi):
    if sayi%2==0:
        return sayi
    else:
        raise ValueError

for i in liste:
    try:
        print(kontrol(i))
    except:
        pass