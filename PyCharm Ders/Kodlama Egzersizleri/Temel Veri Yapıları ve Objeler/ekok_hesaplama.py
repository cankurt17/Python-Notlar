





a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

def ekok(a,b):
    i = 1
    while not(i%a==0 and i%b == 0):
        i+=1
    return i

print("Ekok: ",ekok(a,b))

