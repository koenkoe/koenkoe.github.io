import requests
import os
os.system('cls || clear')
website = input("Voer de URL van de website in (voorbeeld.com): ")

url = ("https://" + website)

try:

    response = requests.get(url)
    if response.status_code == 200:
        print("Website succesvol opgehaald.")
    zoekwoord = input("Welk woord wil je zoeken op de website?: ")
    if zoekwoord in response.text:
        print("Het woord", zoekwoord , "staat op https://" + website )
    else:
        print("Het woord" , zoekwoord , "staat niet op https://" + website )

except requests.exceptions.RequestException as x:
    print(f"Er is een fout opgetreden bij het ophalen van de website: {x}")