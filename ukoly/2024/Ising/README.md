# Isingův model

Isingův model se používá k popisu magnetických vlastností pevné látky. Spočívá v sadě $n$ interagujících "spinů" (magnetických dipólů) $S_j$ uspořádaných na pravidelné mříži. Interakce je krátkodosahová a zahrnuje pouze sousední spiny. Podle uspořádání mříže se rozlišují různé typy a dimenzionality mříží: řetízek (1D mříž), čtvercová nebo šesterečná mříž (2D mříž) nebo různé typy prostorových (3D) mříží. Uvažujte, že každý spin může mít pouze jednu ze dvou hodnot: $S_j=\pm 1$ (spin míří nahoru nebo dolů, jinam mířit nemůže).

Celková energie systému je $$E=-J\sum_{\langle jk\rangle}S_{j}S_{k},$$ kde $J>0$ je konstanta udávající sílu interakce a sčítá se přes všechny sousední spiny, což je naznačeno symbolem $\langle jk\rangle$. Znaménko $-$ zaručuje, že preferované uspořádání spinů je paralelní (všechny spiny míří stejným směrem) a odpovídá feromagnetu.

Střední magnetizace mříže je $$M=\langle S_{j}\rangle=\frac{1}{N}\sum_{j=1}^{N}S_{j},$$ kde $N$ je celkový počet spinů na mříži. Při nulové teplotě se všechny spiny zorientují paralelně a magnetizace je $M=\pm 1$.

Má-li mříž nenulovou teplotu, pak termální fluktuace rozbíjejí paralelní uspořádání spinů. Při nekonečné velikosti mříže $N\rightarrow\infty$ má model termodynamický fázový přechod mezi feromagnetickou fází s $|M|>0$ a paramagnetickou fází $M=0$ na tzv. *Curieho teplotě* $T_{c}$. Numericky lze fázový přechod pozorovat i pro konečnou velikost mříže.

## Metropolisův algoritmus
Isingův model za konečné teploty lze simulovat *Metropolisovým algoritmem*, se kterým jsme se již setkali při minimalizaci pomocí náhodné procházky. Algoritmus spočívá v následujících krocích:
1. Na mříži s celkem $N$ spiny o zadané geometrii zvolíme náhodně orientaci všech spinů.
1. Mříž postupně procházíme a měníme stav (znaménko) každého spinu. Pokud platí, že $\Delta E=E_0-E_1<0$, kde $E_0$ je energie celé mříže před změnou spinu a $E_1$ po změně spinu, pak změnu spinu přijmeme. Pokud naopak $\Delta E>0$, změnu spinu přijmeme s pravděpodobností $$p=e^{-\frac{\Delta E}{k_{B}T}},$$ kde $k_B$ je Boltzmannova konstanta.
1. Získáme nový stav mříže (nový výpočetní krok) a bod 2 opakujeme.

## Úloha
Počítejte stav Isingova systému při teplotě $T$ na dvourozměrné čtvercové mříži velikosti $n\times n$ a celkovém počtu spinů $N=n^2$. Na čtvecové mříži každý spin interaguje se čtyřmi sousedy. Počáteční stav mříže volte náhodně. Poté nechte mříž $r$ časových kroků relaxovat. Následně spočítejte v $m$ krocích energii $E_{k}$ a magnetizaci $M_{k}$ a hodnoty zprůměrujte: $$\bar{E}=\frac{1}{m}\sum_{k=1}^{m}E_{k},\quad \bar{M}=\frac{1}{m}\sum_{k=1}^{m}M_{k}.$$ Vykreslete grafy funkcí $E=E(T)$, $M=M(T)$. Odhadněte Curieovu teplotu.

Program zoptimalizujte tak, aby počítal na co největší mříži (minimálně $20\times 20$). Zvolte vhodně dobu relaxace $r$ a počet bodů k průměrování $m$.
