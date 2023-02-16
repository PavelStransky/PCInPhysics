import matplotlib.pyplot as plt
import math                             # Používáme goniometrické funkce

# plt.ion()                             # Interactive Mode On - pokud spustíme tuto funkci, program nebude zastavovat na plt.show()

xs = [0.1 * i for i in range(100)]      # Hodnoty x od 0 do 10 s krokem 0.1
ys1 = [math.sin(x) for x in xs]         # Funkce sin(x)

plt.plot(xs, ys1)                       # Vykreslení grafu
plt.show()                              # Zobrazení grafu


""" Více grafů v jednom panelu """
ys2 = [math.tan(x) for x in xs]         # Funkce tangens

plt.plot(xs, ys1)
plt.plot(xs, ys2)
plt.show()                              # Ukáže graf. POZOR, Pro pokračování provádění kódu je potřeba graf zavřít (pokud nepoužíváte interaktivní mód plt.ion())

""" Popisky os a grafu"""
plt.plot(xs, ys1, color="red", linestyle=":", label="$\\sin(\\xi)$")
plt.plot(xs, ys2, "b-.", label=r"$\tan(\xi)$")
plt.xlabel(r"$\xi$")                       # Popisky os (lze použít základní příkazy LaTeXu uvozené znaky $$)
plt.ylabel("$y$")
plt.title("Goniometrie")                # Popisek grafu
plt.ylim(-3, 3)                         # Meze osy y
plt.legend()                            # Zobrazí legendu
plt.savefig("d:\\obrazek.pdf")          # Uloží obrázek do souboru
plt.show()

""" Více panelů """
plt.subplot(211)                        # Číslo vyjadřuje počet řádků, počet sloupců a pořadí grafu
plt.plot(xs, ys1)
plt.xlabel("$x$")
plt.ylabel("$\\sin(x)$")

plt.subplot(212)
plt.plot(xs, ys2, color="red", linewidth=3.0)
plt.xlabel("$x$")
plt.ylabel("$\\tan(x)$")
plt.ylim(-3, 3)

plt.suptitle("Goniometrie")             # Hlavní nadpis celého grafu
plt.show()