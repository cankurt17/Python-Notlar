

import requests

url="https://api.exchangeratesapi.io/latest?base="

a=input("Birinci döviz: ")
b=input("İkinci döviz: ")
miktar = float(input("Miktar: "))
response = requests.get(url+a)

json_verisi=response.json()

print(json_verisi["rates"][b]*miktar)