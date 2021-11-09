

a = int(input("a değerini giriniz:"))
b = int(input("b değerini giriniz:"))
c = int(input("c değerini giriniz:"))

delta = (b**2 )- (4*a*c)

birinci_kok = (-b-(delta**0.5))/(2*a)
ikinci_kok = (-b+(delta**0.5))/(2*a)

print("Birinci kök: {}".format(birinci_kok))
print("Birinci kök: {}".format(ikinci_kok))

