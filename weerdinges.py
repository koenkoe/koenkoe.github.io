import requests
Apikey = ""




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
            print(f"{i + 1}: {loc['name']},{loc['state']}, {loc['country']}, {loc['lat']},{loc['lon']}")#print het nummer(1tje hoger) en daarna de informatie die we van de website krijgen
        keuze = int(input("Welke wil je weten")) -1
        return data[keuze]

def getweer(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={Apikey}"

    antwoord = requests.get(url)
    return antwoord.json()

stad = input("Van welke stad wil je het weer zien?:")
land = input("In welk land ligt deze stad?:")
coco = Coordinaten(stad,land)
weer = getweer(coco['lat'], coco['lon'])
print("Welke weerdata wil je zien?:")
opties = {
    "1": "Temperatuur",
    "2": "Luchtvochtigheid",
    "3": "Wind snelheid",
    "4": "Alles"
    }
print(opties)

keuze = input("Kies een optie: ")

weer_huidig = weer
beschrijving = weer_huidig['weather'][0]['description']
print(f"{coco['name']}, {coco['country']}")
if keuze == "1":
    print(f"Temperatuur: {weer_huidig['main']['temp']}°C")
elif keuze == "2":
    print(f"Luchtvochtigheid: {weer_huidig['main']['humidity']}%")
elif keuze == "3":
    print(f"Wind: {weer_huidig['wind']['speed']} m/s")
else:
    print(f"Temperatuur: {weer_huidig['main']['temp']}°C")
    print(f"Luchtvochtigheid: {weer_huidig['main']['humidity']}%")
    print(f"Wind: {weer_huidig['wind']['speed']} m/s")
    print(f"Beschrijving: {beschrijving}")


