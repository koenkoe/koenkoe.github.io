try:
    f = open(r"Jouw Bestand", "r")#Zet hier een (leeg) txt bestand neer
    aantal = int(f.read().strip())
    f.close()  
except (FileNotFoundError, ValueError):
    aantal = 0

aantal += 1
f = open(r"C:Hetzelfde bestand als hierboven", 'w')
f.write(str(aantal))
f.close()  

print(f"Dit programma is",aantal, " keer gestart.")


