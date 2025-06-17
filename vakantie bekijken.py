import requests
import time


Apikey = 
Apikey2 = 




def Coordinaten(stad, land):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={stad},{land}&limit=5&appid={Apikey}"#vraagt de site voor de lon en lat van een stad en land. Om dit te mogen vragen is er een api key nodig
    antwoord = requests.get(url)
    data = antwoord.json() # json zet de tekst van html om naar python
    if not data:
        print("Niet gevonden")
        return None
    if len(data) == 1:
        return data[0]
    else:
        print("Meerdere locaties gevonden")
        for i, loc in enumerate(data):# enumerate zorgt ervoor dat er automatisch een bv een 1 voor komt(hij print het lijstje met het nummer dat de inhoud heeft ervoor)
            print(f"{i + 1}: {loc['name']},{loc.get('state', '')}, {loc['country']}, {loc['lat']},{loc['lon']}")#print het nummer(1tje hoger) en daarna de informatie die we van de website krijgen
        keuze = int(input("Welke wil je weten?:")) -1
        return data[keuze], data[keuze]['country']


def getweer(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={Apikey}"

    antwoord = requests.get(url)
    return antwoord.json()


def valueta(land):
    url1 = f"https://restcountries.com/v3.1/name/{land}"
    ant = requests.get(url1)
    if ant.status_code != 200:
        return None
    data = ant.json()
    print(data[0]['currencies'])

    currencies = data[0].get("currencies", {})
    valutacode = list(currencies.keys())[0]
    print(valutacode)

    return valutacode
def getexchange(land):
    valutacode = valueta(land)
    if not valutacode:
        return f"valutacode niet gevonden voor {land}"
    url = f"https://api.exchangerate.host/live?base=EUR&symbols={valutacode}&access_key={Apikey2}"
    antwoord = requests.get(url)
    data = antwoord.json()
    waarde = data['quotes']['USD' + valutacode]


    return waarde


    
    
stad = input("Van welke stad wil je naartoe?:")
land = input("In welk land ligt deze stad?:")
locatie, landcode = Coordinaten(stad, land)

if locatie is not None:
    weer = getweer(locatie['lat'], locatie['lon'])
    waarde = getexchange(landcode)
    print(f"Weer in {locatie['name']}, {landcode}: {weer}")
    print(f"Wisselkoers USD -> {landcode}: {waarde}")
else:
    print("Kan geen gegevens ophalen.")
score = 10
tempratuur = weer['main']['temp']
if tempratuur <= 30:
    if tempratuur <= 15:
        score -= 3
else:
    score -=  4
if waarde <= 1:
    score -= 2

wind = weer['wind']['speed']
if wind >= 2 :
    score -= (1.5*wind) - 2
elif wind <= 1:
    score -= 1
score = round(score, 2)
print(f"De windkracht is {wind}")

print(f"De temeratuur is {weer['main']['temp']}")
print (f"Je bestemming krijgt een {score}")
