import csv                          # Modul csv (comma-separated values) je součástí instalace Pythonu
import matplotlib.pyplot as plt

file_name = r"python//kafe.txt"     # Cestu k souboru může být potřeba upravit

# Inicializace proměnných
temperatures = []
times = []

t = 0

""" Načtení souboru """
with open(file_name) as file:       # Otevření souboru
    csvReader = csv.reader(file, delimiter='\t')
                                    # Vytvoření csv čtečky; 
                                    # hodnoty v načítaném souboru jsou oddělené tabulátorem \t
    for row in csvReader:        
        if len(row) < 3:            # Odfiltrujeme záhlaví
            continue

        temperatures.append(float(row[1]))
        times.append(t)             # Převod data (času) na číslo bývá otravným úkolem. Vyřešíme oklikou.
        t += 10

plt.plot(times, temperatures, 'o', label="Naměřená data")
plt.xlabel(r"$t\ [s]$")
plt.ylabel(r"$T\ [\degree C]$")
plt.show()

""" Uložení souboru """
with open(r"kafe_out.txt", "w", newline="") as file:
                                    # newline="" je nutný parametr ve windows; jinak program vkládá mezi data prázdné řádky
    csvWriter = csv.writer(file, delimiter='\t')
    csvWriter.writerow(["t [s]", "Texp [C]"])   # Hlavička

 #   for row in zip(times, temperatures):
 #       csvWriter.writerow(row)
        
    csvWriter.writerows(zip(times, temperatures))
