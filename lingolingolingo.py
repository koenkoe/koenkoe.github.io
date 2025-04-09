import random

gameover = 1 
fouten = 0
weergavewoord = ""
inputwoord = ""
woorden = [
    "appel", "boter", "cacao", "draad", "eikel", "fluit", "groot", "hapje", "ijsje", "jacht",
    "kabel", "lepel", "molen", "nacht", "oever", "piano", "quasi", "rodeo", "snoep", "tango",
    "uitje", "vogel", "water", "xenon", "yacht", "zebra", "vloer", "stoel", "bakje", "hondje",
    "klein", "ramen", "stoel", "vrede", "zomer", "winst", "markt", "super", "gloed", "licht",
    "storm", "vogel", "muize", "takje", "regen", "klomp", "stoom", "broek", "fruit", "glans",
    "hoorn", "juist", "kraan", "lucht", "motto", "nacht"
]

hetwoord = random.choice(woorden)
if hetwoord == "hondje":
    print("6 letters..... ik vraag me af wel woord dat is....")

def checkwoord():
    global weergavewoord
    weergavewoord1 = ''
    for letter in range(5):
        if inputwoord[letter] == hetwoord[letter]:
            weergavewoord1 += inputwoord[letter].upper()
        elif inputwoord[letter] in hetwoord:
            weergavewoord1 += inputwoord[letter].lower()
        else:
            weergavewoord1 += "_"
    weergavewoord = weergavewoord1


print("Je hebt 5 kansen om een random 5 letter woord te raden.")    
print("Een hoofdletter betekend dat een letter op de goed plek staat.")
print("Een kleine letter betekend dat die letter in het woord zit maar niet op de goede plek staat.")
print("Een _ betekend dat de letter helemaal niet in het woord zit.")
print("Veel succes!!")


while gameover == 1:
    inputwoord = input("Welk 5-letter woord gok je?: ").strip().lower()
    if len(inputwoord) != 5:
        print("dit woord is niet 5 letters!")
        continue
    checkwoord()
    print(weergavewoord)
    if weergavewoord.lower() == hetwoord:
        gameover = 0
        print("Je hebt gewonnen!")
        break
    if fouten >= 4:
        gameover = 0
        print("Jammer, je hebt verloren, het woord was:", hetwoord)
    fouten += 1
