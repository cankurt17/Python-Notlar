


metin="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for i in metin:
    if i in frekans:
        frekans[i] +=1
    else:
        frekans[i]=1

for i,j in frekans.items():
    print(i+"------->"+str(j))


