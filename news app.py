import json
import os
import requests
from datetime import datetime, timedelta


os.system('cls || clear' )
tijd = datetime.now()
wanneer = int(input(f"Hoeveel dagen terug wil je zoeken?(min 3 max 31):"))
while wanneer >=32 or wanneer <= 2:
    print(f"Ongeldige ")
    wanneer = int(input(f"Hoeveel dagen terug wil je zoeken?(min 3 max 31):"))
tijdtot = tijd - timedelta(days=2)
tijdfrom = tijd - timedelta(days= wanneer)

def MaakURL(host, endpoint, parameters):
    parameterLijst = []
    for key, value in parameters.items():
        parameterLijst.append(f"{key}={value}")

    return f"{host}/{endpoint}?" + '&'.join(parameterLijst)



api_key     = "3397d7fcbb5f4d3a923f22df6d0d383f"


host        = "https://newsapi.org/v2"
endpoint    = "everything"

zoekwoord = input(f"Voor welk woord wil je zoeken?:")
parameters = {
    'apiKey':       api_key,
    'from':         tijdfrom,
    'language':     'nl',
    'page':         1,
    'pageSize':     5,
    'q':            zoekwoord ,
    'searchIn':     'title,description,content',
    'sortBy':       'relevancy',
    'to':           tijdtot,
}


url = MaakURL(host, endpoint, parameters)


response = requests.get(url)
data = response.json()

artikelen = data.get('articles', [])

if artikelen:
    for i, artikel in enumerate(artikelen, 1):
        print(f"Artikel {i}:")
        print(f"Titel      : {artikel.get('title')}")
        print(f"Samenvatting: {artikel.get('description')}\n")
else:
    print("Geen nieuws gevonden.")

try:
    lezen = int(input("\nWelk artikel wil je volledig bekijken? (1 t/m 5): "))
    if 1 <= lezen <= len(artikelen):
        gekozen_artikel = artikelen[lezen - 1]
        print("Volledig artikel:")
        print(f"Titel      : {gekozen_artikel.get('title')}")
        print(f"Inhoud     : {gekozen_artikel.get('content') or 'Geen volledige inhoud beschikbaar.'}")
        print(f"URL        : {gekozen_artikel.get('url')}")
    else:
        print("Ongeldige keuze. Kies een getal uit de lijst.")
except ValueError:
    print("Ongeldige invoer. Voer een getal in.")
