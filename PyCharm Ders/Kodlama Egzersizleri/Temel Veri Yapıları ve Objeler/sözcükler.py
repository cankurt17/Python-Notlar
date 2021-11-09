

birler= {0:"",1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}
onlar= {0:"",1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elii",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan"}

sayi = int(input("Sayi: "))

def okunus(sayi):
    bir = sayi%10
    on = sayi//10
    return onlar[on] +" "+ birler[bir]
print(okunus(sayi))