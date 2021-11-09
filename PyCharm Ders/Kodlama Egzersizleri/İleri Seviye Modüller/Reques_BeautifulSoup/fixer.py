import requests

api_key = "e2266c4e1c73220ffb50633a2caecdf7"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

a = input("Birinci Para Birimi:")  # Örnek : USD
b = input("İkinci Para Birimi:")  # Örnek : TRY
amount = int(input("Miktar:"))  # Örnek: 15

response = requests.get(url)

infos = response.json()

USD = infos["rates"][a]
TRY = infos["rates"][b]

print((TRY / USD) * amount)



