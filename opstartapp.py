try:
    f = open(r"C:\Users\Koen Hoefsloot\Desktop\opstart.txt", "r")
    aantal = int(f.read().strip())
    f.close()  
except (FileNotFoundError, ValueError):
    aantal = 0

aantal += 1
f = open(r"C:\Users\Koen Hoefsloot\Desktop\opstart.txt", 'w')
f.write(str(aantal))
f.close()  

print(f"Dit programma is",aantal, " keer gestart.")


