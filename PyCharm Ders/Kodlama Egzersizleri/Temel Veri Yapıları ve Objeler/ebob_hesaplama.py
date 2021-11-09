



a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

def ebob(a,b):

    if a <= b:
        j =a
    else:
        j =b
    for i in range(j,0,-1):
        if a%i==0 and b%i==0:
            return i

print("Ebob: ",ebob(a,b))
