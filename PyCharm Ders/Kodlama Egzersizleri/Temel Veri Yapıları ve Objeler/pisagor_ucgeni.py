
liste = list()
def pisagor():
    for a in range(1,101):
        for b in range(1,101) :
            for c in range(1,101):
                if a<b<c:
                    if c**2 == a**2 + b**2:
                        liste.append([a,b,c])

    return liste
for i in pisagor():
    print(i)