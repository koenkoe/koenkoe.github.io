import random
nietgerade = "qwertyuiopasdghjklzxcvfbnm" 
welgerade = ""
typewoord = input("Wil je zelf een woord invullen?:")
lijstwoorden = "appel","informatica","galgje","laptop","koen","pinguin","printer","vodka","clv","gasfornuis",""
if typewoord == 'ja':
    hetwoord = input("Vul hier je woord in: ")
else:
    hetwoord = random.choice(lijstwoorden)
maxfout = 10
fouten = 0
weergavewoord = '_'
goed = 0
print("\033c", end="") #Dit heb van internet#

while fouten < maxfout:
    if '_' in weergavewoord:
        geradeletter = input("Welke letter gok je:")
        if geradeletter in nietgerade:
            nietgerade = nietgerade.replace(geradeletter, '')
            welgerade = welgerade + geradeletter
            if geradeletter in hetwoord:
                print('Deze letter is GOED!!!!')
            else:
                print('Ai das nie goed :( ')
                fouten +=1
                print('Je hebt nog', maxfout - fouten,'keuzes over!' )
            weergavewoord = hetwoord
            for letter in nietgerade:
                weergavewoord =  weergavewoord.replace(letter, '_')
            print( weergavewoord)
        else:
            print('Deze letter is al geraden. Je hebt nog keuze uit ', nietgerade)
    else:
        goed = 1
        fouten = maxfout

if goed == 1:
    print('Gefeliciteerd, je hebt', hetwoord, 'geraden!')    
else:
    print('Dat is jammer, je bent af')
    print('Het woord was', hetwoord)