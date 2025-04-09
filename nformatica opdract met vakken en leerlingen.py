l = open(r"C:\Users\Koen Hoefsloot\Downloads\2025_04_09_leerlingen.txt", "r")
v = open(r"C:\Users\Koen Hoefsloot\Downloads\2025_04_09_vakken.txt", "r")
h = 0
meerdere = []



naamin = input("Welke naam wil je bekijken?:")
for line in l:
    line = line.replace(","," ")[:-1]
    delen = line.split()
    naam = delen[1]
    if naam.lower() == naamin.lower():
        meerdere.append(delen[2]+" "+delen[3]+" "+delen[0])


if len(meerdere) == 0:
    print("Naam niet gevonden!")
if len(meerdere) == 1:
    print(meerdere[0])
    goede = meerdere[0]
        
else:
    for s in range(len(meerdere)):
        print(s, "", meerdere[s])
    check = int(input("Welke achternaam komt overeen? (cijfer): "))
    goede = meerdere[check]



deel2 = goede.split()
leerlingnummer = deel2[2]
print(leerlingnummer)
print(naamin, deel2[0]," heeft deze vakken:")
for line in v:
    line = line.replace(","," ")[:-1]
    delen3 = line.split()
    if leerlingnummer == delen3[0]:
        print(delen3[1])


