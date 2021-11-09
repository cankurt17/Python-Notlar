
def kontrol(x):
    a=x[0]
    b=x[1]
    c=x[2]
    if (abs(b-c)<a<b+c) and (abs(a-c)<b<a+c) and (abs(a-b)<c<a+b):
        return True
    else:
        return False

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(kontrol,liste)))