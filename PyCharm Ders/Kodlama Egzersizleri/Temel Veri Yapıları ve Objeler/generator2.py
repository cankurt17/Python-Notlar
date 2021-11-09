


def asal():
    for i in range(2,1000):
        s=0
        if i == 2:
            yield i
        else:
            for j in range(2,i):
                if i%j==0:
                    s+=1
            if s==0:
                yield i

for i in asal():
    print(i)