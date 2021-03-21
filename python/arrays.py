import numpy as np                      # Knihovna numpy se obvykle označuje zkráceným np (konvence)

""" Řady ze seznamů """
x = np.array([1, -1, 2, -2, 3, -3])     # Vytvoření celočíselné řady ze seznamu čísel
print(x.dtype)          # = "int32"     # Základní typ celočíselné řady

y = np.array([0.5, 1, 2, 4, 8, 16])     # Pokud je jeden prvek neceločíselný, řada je neceločíselná
print(y.dtype)          # = "float64"   # Základní typ neceločíselné řady

i = np.array([1, 2, 3.14], dtype="int8")# V odůvodněných případech lze typ zadat explicitně (v tomto případě 8bitové celé číslo)

"""  Speciální řady """
s = np.linspace(0, 1, 30)               # Řada 30 čísel rovnoměrně pokrývající interval 0 a 1 (včetně koncových bodů)
r = np.arange(0, 1, 0.1)                # Řada čísel mezi 0 a 1 s krokem 0.1

o = np.zeros((4, 5, 6))                 # Vytvoří třírozměrnou řadu o rozměru 4 x 5 x 6 a vyplní ji nulami
z = np.ones((10, 10))                   # Vytvoří dvourozměrnou řadu (matici) o rozměru 10 x 10 a vyplní ji jedničkami
i = np.identity(4)                      # Vytvoří jednotkovou matici rozměru 4 x 4
f = np.full((3, 4), np.pi)              # Matice, jejíž všechny elementy budou pi

print(o.ndim)           # = 3           # Počet rozměrů řady
print(o.shape)          # = (4, 5, 6)   # Tvar řady
print(o.size)           # = 120         # Celkový počet prvků řady

sm = s.reshape((3, 10))                 # Změní tvar řady; počet elementů se musí zachovat
print(sm)

t = sm.transpose()                      # Transpozice

""" Algebraické operace """
z = x - y                               # Mají-li řady stejný počet prvků, lze s nimi takto jednoduše pracovat
w = x * y
print(w.dtype)                          # Výsledný typ je vždy ten nejpřesnější z typů jednotlivých operandů

m = np.dot(sm, t)                       # Maticové násobení - rozměry matic musí být kompatibilní!
x.dot(y)                                # Skalární součin vektorů

""" Náhodné operace """
r = np.random.rand(3, 5)                # Matice rozměru 3 x 5 vyplněná náhodnými čísly z rovnoměrného rozdělení na <0, 1)
np.random.shuffle(sm)                   # Náhodně promíchá řadu (na místě)
ri = np.random.randint(0, 100, (3, 5))  # Matice rozměru 3 x 5 vyplněná náhodnými celými čísly 0 <= d < 100
rn = np.random.normal(0, 1, (3, 5))     # Matice rozměru 3 x 5 vyplněná náhodnými Gaussovsky rozdělenými čísly (mu = 0, sigma = 1)