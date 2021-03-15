# Jednořádkový komentář

""" Víceřádkové komentáře se zapisují stejně jako víceřádkový text,
    a to mezi troje uvozovky nebo apostrofy.
"""

####################################################
##### 1. Základní datové typy a operátory
####################################################

""" Celá čísla (int) """
3 

""" Čísla s desetinnou čárkou (float) """
3.14
6.62E-34            # Planckova konstanta v SI

""" Aritmetické operace """
1 + 1               # = 2           # sčítání
8 - 1               # = 7           # odčítání
10 * 2              # = 20          # násobení
35 / 5              # = 7.0         # Dělení vždy vrací číslo s desetinnou čárkou
5 // 3              # = 2           # Pokud se nejedná o speciální celočíselné dělení, kdy je desetinná část oříznuta 
-5 // 3             # = -2          # (platí i záporná čísla)
7 % 3               # = 1           # Modulo (zbytek po celočíselném dělení 
2**4                # = 16          # Mocnění (x na y-tou)

3 * 2.0             # = 6.0         # Pokud je jeden operand desetinným číslem, výsledek je jím také

(1 + 3) * 2         # = 8           # Závorky pro změnu priority operátorů

""" Logické hodnoty """
True
False

""" Logické operátory """
False or True       # = True        # Logický součet
True and False      # = False       # Logický součin
not True            # = False       # Negace


""" Porovnávání """
2 == 1              # = False       # rovnost
2 != 1              # = True        # nerovnost
1 < 10              # = True        # menší
1 > 10              # = False       # větší
2 <= 2              # = True        # menší a rovno
2 >= 2              # = True        # větší a rovno

# Porovnání se dají řetězit!
1 < 2 < 3           # = True
2 < 3 < 2           # = False

""" Řetězce """
# Řetězce se uvozují " nebo '
"Toto je řetězec."
'Toto je také řetězec.'

# Víceřádkové řetězce se uvozují """ nebo '''
''' Toto je jedna možnost,
jak zapsat víceřádkový řetězec '''

# Slučování řetězců
"Rychlost " + "světla"  # = "Rychlost světla"
"Rychlost " "světla"    # = "Rychlost světla"   # (není potřeba psát operátor +)

"Kvantová chromodynamika"[0]    # = 'K'         # Řetězec je seznam znaků, lze tedy indexovat

""" Formátování řetězců """
hbar = 1.054572E-34

# Použití metody format ("New Style" formátování)
# https://docs.python.org/3/library/string.html#formatstrings
"{} konstanta má hodnotu {} {}".format("Redukovaná Plackova", hbar, "Js") 
                        # = "Redukovaná Planckova konstanta má hodnotu 1.054572e-34 Js"
"{nazev} konstanta má hodnotu {hodnota} {jednotka}".format(nazev="Boltzmannova", hodnota=1.380649E-23, jednotka="J/K")                     
                        # Hodnoty lze pojmenovat
"Komu se ne{rym}, tomu se ze{rym}".format(rym="lení")   
                        # Označení se může ve formátovaném řetězci libovolně opakovat

# Interpolace (f - řetězec)
f"Redukovaná Planckova konstanta má hodnotu {hbar} Js"  
f"Její druhá mocnina je {hbar**2} (Js)^2"   # Mezi závorky lze vložit jakýkoliv výraz

# Použití printf formátování z programovacího jazyka C ("Old Style" formátování)
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
"%s konstanta má hodnotu %e %s" % ("Avogadrova", 6.022141E+23, "mol^-1")

""" Speciální znaky """
# Některé znaky se zapisují pomocí pomocného symbolu \ (například \t - tabulátor, \n - nový řádek, \\ - znak \)
print("x1\tx2\ny1\ty2")             # Převede speciální znaky na symboly (tento řetězec vypíše jako tabulku 2x2)
print(r"x1\tx2\ny1\ty2")            # Vypíše řetězec tak, jak je (raw string)

""" Prázdná hodnota """
None

""" Přetypování """
int(2.82)               # = 2       # float to int
float("9.34")           # = 9.34    # string to float
str(3.14)               # = "3.14"  # float to string
bool(0)                 # = False   # int to bool (všechny hodnoty jsou True jen 0 je False)

####################################################
##### 2. Proměnné a kolekce
####################################################
# Python je case-sensitive, záleží tedy na velikosti písmen.
# Proměnné není třeba deklarovat před přiřazením a není potřeba specifikovat jejich typ.
# Konvence je používat male_pismo_s_podtrzitky (underscore style).
# Lze pojmenovávat jakkoliv, klíčová je hlavně konzistence.
# Kód je čitelnější, pokud podle pojmenování proměnné ihned víme, co obsahuje.
pocet_kraju = 14
# Názvy proměnných mohou obsahovat i unicode znaky, například písmena s diakritikou, ale nedoporučuji to.
# Naopak doporučuji používat anglické pojmenování proměnných, protože nikdy nevíte, kdo bude váš kód používat.
počet_krajů = 14

del počet_krajů                     # Odstraní proměnnou

pocet_kraju += 2                    # Zvýšení počtu krajů o 2

# V Pythonu neexistuje operátor ++

""" Seznamy (lists) """
otevrena_divadla = []               # Prázdný seznam
fibonacci = [1, 1, 2, 3, 5]         # Začátek Fibonacciho řady


fibonacci.append(8)                 # Na konec seznamu se přidává pomocí append
fibonacci.pop()                     # pop naopak z konce řady prvek odstraní

fibonacci[0]        # = 1           # Python indexuje od 0, takže toto je první prvek
fibonacci[-1]       # = 5           # Lze indexovat i odzadu

fibonacci.append(fibonacci[-1] + fibonacci[-2]) # Takto můžeme postupně přidávat další prvky Fibonacciho řady

5 in fibonacci      # = True        # Kontrola, jestli prvek 5 v seznamu existuje
len(fibonacci)      # = 6           # Délka seznamu

# Řezy (slices)
fibonacci[0:2]      # = [1, 1]      # Vybere prvky s indexy 0 a 1 (dolní mez včetně, horní mez nikdy; počet vybraných prvků je tedy horní-spodní mez)
fibonacci[3:]       # = [3, 5, 8]   # Prvky od indexu 3 do konce seznamu
fibonacci[:3]       # = [1, 1, 2]   # 3 prvky od začátku řady
fibonacci[::2]      # = [1, 2, 5]   # Každý druhý prvek
fibonacci[::-1]     # = [8, 5, 3, 2, 1, 1]  # Seznam v opačném pořadí

# [zacatek:konec:krok] == slice(zacatek, konec, krok)

# Kopie seznamu
f = fibonacci               # POZOR! Provede tzv. mělkou kopii, tj. f a fibonacci ukazují na stejné místo v paměti
f[0] = -1
print(f)                    # = [-1, 1, 2, 5, 8]
print(fibonacci)            # = [-1, 1, 2, 5, 8]
f = fibonacci.copy()        # Pro opravdovou kopii seznamu nutné pooužít buď metodu copy()...
f = fibonacci[:]            # ...nebo řez

# Slučování seznamů
fibonacci + [13, 21]        # = [1, 1, 2, 3, 5, 8, 13, 21]
fibonacci.extend([13, 21])  # totéž

pelmel = [0, "Ryba", fibonacci, hbar]   # Prvky seznamu nemusejí mít stejné typy; prvky seznamu mohou být i seznamy

# Rozbalení seznamů a n-tic
otevrena_divadla, zivocich, fibonacci, hbar = pelmel
print(zivocich)             # = "Ryba"

a, b = 10, 20               # Pomocí rozbalení lze přiřazovat více proměnných zároveň
a, b = b, a                 # A takto jednoduše prohodíme hodnoty dvou proměnných

""" N-tice (tuples)"""
# Jako seznam, ale nelze měnit prvky seznamu
ntice = (2, 4, 6)
ntice = (1,)                # Pokud chceme n-tici s jedním prvkem, musíme použít tento zápis

""" Slovníky """
# Neuspořádané množiny, kdy každý element má vlastní klíč a hodnotu
cena = {"mleko": 19.9, "chleba": 32.5, "kvetak": 48.2}

cena["chleba"]          # = 32.5                            # Indexuje se pomocí klíče
list(cena.keys())       # = ["chleba", "mleko", "kvetak"]   # Seznam klíčů; není zaručeno pořadí
list(cena.values())     # = [48.2, 32.5, 19.9]              # Seznam hodnot; opět není zaručeno pořadí

"kvetak" in cena        # = True                            # Kontrola, jestli prvek s klíčem "květák" v seznamu existuje

cena["cokolada"] = 24.9 # Přidá nový prvek do slovníku
del cena["mleko"]       # odebere prvek s klíčem "mléko" ze slovníku

""" Množiny (sets)"""
# Neuspořádané množiny bez duplicitních údajů
prvocisla = {2, 3, 5, 7, 11, 13}

prvocisla.add(23)       # Přidání prvku
prvocisla.add(3)        # Prvek v množině už je, množinu to tudíž nezmění

dvouciferna_prvocisla = {11, 13, 17, 19, 23}
prvocisla & dvouciferna_prvocisla   # = {11, 13, 23}                        # Průnik
prvocisla | dvouciferna_prvocisla   # = {2, 3, 5, 7, 11, 13, 17, 19, 23}    # Sjednocení
prvocisla - dvouciferna_prvocisla   # = {2, 3, 5, 7}                        # Rozdíl

####################################################
## 3. Řízení toku programu, cykly
####################################################
# Bloky kódu musí být odsazeny a musí mít stejné odsazení

""" Podmínka """
if otevrena_divadla > 1:
    print("Hurá, jdeme za kulturou. A je z čeho vybírat.")
elif otevrena_divadla == 1:         # Část elif je nepovinná; může jich být ale i více
    print("Jedno divadlo. Rychle koupit lístky")
else:                               # Část else je také nepovinná
    print("Vše zavřené. Korona.")

""" Cyklus """
# Provádí se přes jakýkoliv iterovatelný objekt
for fyzik in ["Einstein", "Dirac", "Feynman"]:
    print(f"{fyzik} byl génius.")

for zbozi in cena.keys():   # cena.keys() je iterovatelný objekt, lze ho takto vypsat
    print(zbozi)

# Chceme-li iterovat přes celá čísla, použijeme range
for i in range(10):         # Vypíše čísla od 0 do 9 včetně (deset čísel)    
    print(i)        

for j in range(10, 20, 3):  # Vypíše čísla od 10 (včetně) do 20 s krokem 3
    print(j)        

""" Smyčka """
while len(fibonacci) < 10:  # Provádí smyčku do té doby, dokud je splněna podmínka (dokud nemá seznam fibonacci deset prvků)
    fibonacci.append(fibonacci[-1] + fibonacci[-2])    

# Ve smyčce a cyklu lze použít klíčová slova continue (pro okamžité provádění další iterace) a break (pro okamžité ukončení)
while True:                             # Nekonečná smyčka
    zadani = input('Zadejte řetězec: ') # Zadání z klávesnice
    if len(zadani) > 5:                 # Je-li délka slova větší než 5...
        print("V pořádku. Končím.")
        break                           # ...smyčku ukončíme
    print(f"Řetězec {zadani} je příliš krátký. Zadejte znovu.")

####################################################
## 4. Funkce
####################################################
# Stejně jako v případě cyklů, i zde je tělo funkce v odsazeném bloku

def odecti(x, y=1):      # Funkce (metoda) se definuje klíčovým slovem def; můžeme zadat i implicitní hototy argumentů
    """
        Vložíme-li takovýto komentář bezprostředně pod deklaraci funkce,
        slouží jako dokumentační komentář (docstring) a lze k němu přistoupit přes atribut __doc__.
        Zobrazí se také v našeptávači Visual Studio Code, pokud nad název funkce najedeme myší.
    """
    return x - y        # Hodnoty se vrací pomocí return

odecti(5, 3)            # = 2       # Volání funkce
odecti(y=7, x=10)       # = 3       # Všechny argumenty lze používat jako pojmenované a předávat v libovolném pořadí
odecti(5)               # = 4       # Druhý argument nezadáváme, použije se implicitní hodnota -1

odecti({1, 3, 4}, {3, 5})           # Dynamické typování zabezpečí, že funkce proběhne pro všechny proměnné, pro které má smysl (v tomto případě pro dvě množiny).
                                    #  POZOR, používejte s rozmyslem a konzistentně.

print(odecti.__doc__)               # Vypíše komentář k funkci

# Python neumožňuje přetěžování funkcí (jako většina objektových programovacích jazyků).
# Pokud chceme funkci s proměnným množstvím argumentů, použijeme v deklaraci 
# operátor * (pojmenování args je jen konvence) pro všechny nepojmenované argumenty; typ args je n-tice
# operátor ** (kwargs je opět jen konvence) pro všechny pojmenované argumenty; typ kwargs je slovník
def promenne_mnozstvi_argumentu(x, y, *args, **kwargs):
    print(f"x = {x}, y = {y}")
    print(f"Nepojmenované dodatečné argumenty: {args})")
    print(f"Pojmenované dodatečné argumenty: {kwargs}")

# Při volání funkce musíme nejprve zadat povinné argumenty, potom nepojmenované volitené a až nakonec všechny pojmenované
promenne_mnozstvi_argumentu(5, 3, 2, 1, 0, z=5, nazev="Cisla") 

""" Pokročilejší použití funkcí """
def vyrobit_scitacku(pricitane_cislo):
    def scitacka(x):
        return x + pricitane_cislo
    return scitacka

pricist_10 = vyrobit_scitacku(10)
pricist_10(3)       # = 13

# Anonymní funkce
def vyrobit_nasobicku(nasobene_cislo):
    return lambda x: x * nasobene_cislo     # Pomocí klíčového slova lambda

nasobit_2 = vyrobit_nasobicku(2)
nasobit_2(10)

print(pricist_10.__name__)          # Jméno funkce
print(nasobit_2.__name__)           # Funkce je opravdu anonymní

""" Základní prvky funkcionálního programování """
# Lze použít funkce map() a filter() z funkcionálního programování
f_10 = map(pricist_10, fibonacci)   # Vytvoři iterovatelný objekt s elementy Fibonacciho řady zvětšenými o 10
for x in f_10:                      # Ověření, že to funguje (pozor, lze iterovat pouze jednou)
    print(x)                        

flt = filter(lambda x: 10 <= x <= 30, fibonacci)    # Hodnoty Fibonacciho řady v daných mezích
for x in flt:                       # Ověření, že to funguje
    print(x)                        

""" Generátorová notace """
# Vytvoří přímo seznam (zabírá více paměti)
f_10 = [pricist_10(x) for x in fibonacci]       # [11, 11, 12, 13, 15, 18, 23, 31, 44, 65]
flt = [x for x in fibonacci if 10 <= x <= 30]   # [13, 21]

druhe_mocniny = {x: x**2 for x in range(1, 5)}  # => {1: 1, 2: 4, 3: 9, 4: 16}  # Slovník druhých mocnin
hlasky = {pismeno for pismeno in "abeceda"}     # => {"d", "a", "c", "e", "b"}  # Množina

####################################################
## 5. Moduly
####################################################
# Každý soubor projektu lze chápat jako modul.
# Knihovny jsou také jen na určitém místě uložené Pythonovské soubory s funkcemi.
# Existují tři způsoby, jak importovat a pracovat s moduly.

""" 1. Načtení celého modulu """
import math             # Modul s matematickými funkcemi
print(math.sqrt(16.0))  # = 4 (odmocnina)

# Modul lze přejmenovat při importu
import math as m
print(m.sin(m.pi / 6))  # = 0.5

""" 2. Načtení vybraných funkcí z modulu """
from math import ceil, floor
print(ceil(3.7))        # = 4.0     # Horní celá část
print(floor(3.7))       # = 3.0     # Dolní celá část

""" 3. Načtení všech funkcí z modulu """
from math import *      # Silně nedoporučované - může docházet ke kolizím jmen, pokud se funkce s daným jménem vyskytuje ve více modulech

# Funkcí dir() lze zjistit, co všechno modul obsahuje
dir(math)

####################################################
## 5. Třídy
####################################################
class Bod:                              # Deklarace třídy
    dimenze = "rovina"                  # Atribut třídy - je sdílený všemi instancemi
    
    def __init__(self, x, y):           # Kostruktor. Volán, když vytváříme instanci třídy.
        self.x = x                      # Přiřazení parametru do atributu instance
        self.y = y

    def otoc(self, uhel):               # Metoda instance. Všechny metody instance musejí mít "self" jako první parametr (označení self je konvence, lze použít třeba this známé z jiných objekových jazyků)
        self.x = self.x * math.cos(uhel) + self.y * math.sin(uhel)
        self.y = -self.x * math.sin(uhel) + self.y * math.cos(uhel)

    def __str__(self):                  # Převede instanci na řetězec
        return f"x = {self.x}, y = {self.y}"

    @classmethod                        # Metoda třídy sdílená všemi instancemi.
    def vypis_dimenzi(cls):
        print(cls.dimenze)

    @staticmethod                       # Statická metoda je volána bez reference na třídu nebo instanci
    def vypis_():
        return "*ehm*"

# Vytvoření instance
p = Bod(5, 0)
q = Bod(1, 1)

print(p)
p.otoc(math.pi)
print(p)

p.y = 0                                 # V Pythonu jsou všechny atributy veřejné a lze je měnit
print(p)

# Volání třídní metody
p.vypis_dimenzi()       # = "rovina"

# Změna atributu třídy
Bod.dimenze = "2D"
p.vypis_dimenzi()       # = "2D"
q.vypis_dimenzi()       # = "2D"

# Volání statické metody
Bod.vypis_()  # => "*ehm*"


