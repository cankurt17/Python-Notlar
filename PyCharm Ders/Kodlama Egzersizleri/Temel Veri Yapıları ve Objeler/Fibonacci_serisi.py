

print("""
**************************
    Fibonacci Serisi
**************************  
""")


a=1
b=1

fibonacci = [a,b]
print(*range(20))

for i in range(20):
    (a,b) = (b,a+b)
    fibonacci.append(b)
print(fibonacci)
