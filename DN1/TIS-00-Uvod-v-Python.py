# Tako se piše enovrstični komentar

""" 
(Nepravi večvrstični komentar) 
Večvrstični niz, ki se uporablja za dokumentiranje funkcij (docstring).
Ni pravi komentar, se pravi, da se ne ignorira med izvajanjem.
Kakorkoli, tudi nobene "akcije" (kode) ne povzroči ;)
"""

# Pisanje "lepe" kode - slogovna pravila PEP8 (Python Enhancements Proposal)
#   - zamik: 4 presledki (nastavitve v IDE)
#   - en presledek pri operatorju =, torej: a = 5 in ne a=5,
#   - spremenljivke in imena funkcij naj bodo opisne, pišemo jih s podčrtajem: 
#     sirina_valja = 5,
#   - za razrede uporabljamo t.i. format CamelCase, npr. SirinaValja
#   - pri aritmetičnih operatorjih postavimo presledke po občutku: 
#     x = 3*a + 4*b ali x = 3 * a + 4 *b,
#   - za oklepajem in pred zaklepajem ni presledka, prav tako ni 
#     presledka pred oklepajem ob klicu funkcije: 
#     x = sin(x), ne pa x = sin( x ) ali x = sin (x),
#   - presledek za vejico: range(5, 10) in ne range(5,10),
#   - brez presledkov na koncu vrstice ali v prazni vrstici,
#   - znotraj funkcije lahko občasno dodamo po eno prazno vrstico,
#   - med funkcije postavimo dve prazni vrstici,
#   - vsak modul uvozimo (import) v ločeni vrstici
#   - najprej uvozimo standardne pythonove knjižnice, 
#     nato druge knjižnice (npr. numpy) in na koncu lastne.
#
# Opomba: V VS Code pritisnite Ctrl+Shift+P ter napišite "Format document" 
# in pritisnite ENTER za samodejno oblikovanje kode po PEP8.

###############################################################################
# Osnovni podatkovni tipi
###############################################################################
# Python ima dinamično tipiziranje, kar pomeni, da se tip objekta določi pri 
# dodelitvi vrednosti.
# Veljavno ime objekta se začne z [a...zA...Z_] in nadaljuje z 
# [a...zA...Z_0...9] ter ni rezervirana beseda (npr. for, in, is, if, del).
# Dobri primeri: x, x42, _private, Fibonacci
# Slabi primeri: 42a, for (rezervirana beseda), sum (to je vgrajena funkcija)

# Osnovni tipi (razredi): NoneType, bool, int, float, str, bytes
#------------------------------------------------------------------------------
# None je konstanta, ki pomeni nič in je tipa NoneType
nic = None      
# Ta tip vračajo funkcije, ki ne vračajo ničesar. 
# Podobno kot NULL ali void v C.

#------------------------------------------------------------------------------
# Tip bool (Boolean)
t = True        
f = False

# Kratka prekinitev: uporabimo nekaj zanimivih funkcij
print(type(f))    # Izpišemo tip objekta
# help(type)      # help() prikaže dokumentacijo funkcije v argumentu

#------------------------------------------------------------------------------
# Tip int (cela števila), poljubno dolga (do omejitev pomnilnika)
a = 42
#------------------------------------------------------------------------------
# Tip float (realna števila, zapis v plavajoči vejici, dvojna natančnost = 8 B)
b = 3.14
#------------------------------------------------------------------------------
# Tip complex (kompleksna števila)
c = 3 + 2j      # ali z uporabo funkcije ("konstruktorja"): c = complex(3,2)
c.imag 
c.real
#------------------------------------------------------------------------------
# Tip str (niz, podpora Unicode); dvojni in enojni narekovaji imajo isti pomen.
s0 = "Python in TIS"
Σ = "π = 3.141592653589793..."  # Uporaba Unicode
# Če niz vsebuje enojne narekovaje, ga ogradimo z dvojnimi.
s2 = "Python in 'TIS'"
# Če niz vsebuje dvojne narekovaje, ga ogradimo z enojnimi.
s3 = 'Python in "TIS"'
# Uporaba trojnih narekovajev, če znotraj uporabljamo enojne in dvojne
s4 = ''''Python' in "TIS"'''
# Pisanje niza v več vrstic, ampak zgolj v kodi. Pri izpisu želimo eno vrstico.
s5 = "To besedilo " \
    "se mi zdi predolgo" \
    "za eno vrstico urejevalnika." 
# Enako kot prej, samo brez poševnic in z oklepaji
s6 = ("To besedilo "
    "se mi zdi predolgo "
    "za eno vrstico urejevalnika.")

#------------------------------------------------------------------------------
# Prirejanje malo globlje
x = y = z = 1     # Prirejanje iste vrednosti več objektom hkrati
a, b, c = 1, 2, 3 # Prirejanje različnih vrednosti hkrati
a, b = b, a       # Menjava vrednosti (na desni strani smo definirali terko)

# Razpakiranje zaporedja
prvi, drugi, tretji = "ABC"    # prvi vsebuje "A", drugi "B", tretji "C" 
prvi, *ostali = "ABCČDEFZŽ"    # prvi vsebuje "A", ostali pa je seznam ostalih
prvi, drugi, *ostali = "ABCČDEFZŽ"
*ostali, zadnji = "ABCČDEFZŽ"
del x                          # Brisanje imena (del je stavek, ne funkcija)

# Razširjeno prirejanje
# +=, -=, *=, /=, %=, **=
i = 0
i += 1  # i = i + 1
# i++ tu ne obstaja

#------------------------------------------------------------------------------
# Pretvarjanje tipov
bool(None)      # bool() vrne False za: False, 0, None, prazen niz, terko, 
                #                       seznam, množico, slovar ipd.; 
                #                       vse ostalo je True.
int(22.2)
int("22")
int("22", 3)    # številska osnova je 3 - gre za trojiško število, ki ima 
                # desetiško vrednost 8
float(22)
float("22e4")
str(22)         # Vrne niz za prikaz
chr(65)         # Koda ASCII -> znak
ord("A")        # Koda ASCII <- znak

###############################################################################
# Logični operatorji 
###############################################################################
# Navedeni po naraščajoči prioriteti:
#   - x or y:  disjunkcija; drugi element se računa samo, če je prvi neresničen
#   - x and y: konjunkcija; drugi element se računa samo, če je prvi resničen 
#   - not x:   negacija, npr. not 5 -> False
# POZOR: Logična operatorja and in or vračata VREDNOST, pri kateri se je 
# računanje ustavilo. Pri tem upoštevamo, da delujeta kratkostično.
l1 = True and False 
l2 = True or False 
l3 = True and not False or False
l4 = 5 or False
l5 = "Python" or "MATLAB"
l6 = "Python" and "MATLAB"

###############################################################################
# Primerjalni operatorji
###############################################################################
# ==, !=, <, <=, >, >=
"Python" == "PYTHON" # Primerjamo lahko nize (ali v splošnem objekte)
a = 0.5
-1 <= a <= 1         # Nizanje primerjanj
a > 0 or a < -1      # Veriženje primerjanj

###############################################################################
# Aritmetični operatorji in funkcije
###############################################################################
# Navedeni po naraščajoči prioriteti:
# +     vsota
# -     razlika
# *     množenje
# /     deljenje
# //    celoštevilsko deljenje
# %     ostanek pri celoštevilskem deljenju
# -x    negacija
# abs() absolutna vrednost
# **    potenca (ali funkcija pow())
x1 = 3 / 2
x2 = 3 // 2
x3 = abs(-42)   # Klic funkcije za absolutno vrednost
x4 = abs(2+3j)  # Deluje tudi za kompleksna števila
x5 = 2**3       # Potenca, lahko tudi pow(2, 3)
x6 = 2.1**3.14  # Osnova in potenca sta lahko realni števili
x7 = (-1)**0.5  # Negativna osnova nam da kompleksno število

###############################################################################
# Bitni operatorji
###############################################################################
~5     # negacija bitov 
       # 0...0101 -> 1...1010 (to v dvojiškem komplementu predstavlja -6)
5 | 3  # bitni ali: 101 | 011 = 111 (7 desetiško)
5 & 3  # bitni in:  101 & 011 = 001 (1 desetiško)
5 ^ 3  # ekskluzivni ali: 101 ^ 011 = 110 (6 desetiško)
5 << 3 # premik bitov za 3 v levo: 101 -> 101000 (40)
5 >> 3 # premik bitov za 3 v desno: 101 -> 0

###############################################################################
# Stavek if
###############################################################################
# Zamiki so poljubni, vendar morajo biti konsistentni (če zamikamo za 3 
# presledke, moramo to delati v celi datoteki s kodo)
d = 0
if d > 0:
    niz = 'pozitiven'
elif d < 0:
    niz = 'negativen'
else:
    niz = 'nicla'
print(niz)

# Kompaktna oblika pogojnega stavka - izraz if (trojiški operator ?: v Cju)
x = 22 if 42 % 12 >= 3 else -1  # x = 42 % 12 >= 3 ? 22 : -1

###############################################################################
# Zanki while in for
###############################################################################
vsota = 0
i = 1
while i < 20:
    vsota = vsota + i
    i = i + 2
else:  # neobvezen del, izvede se, ko pogoj ni (več) resničen in zanka ni bila prekinjena z break
    print(vsota)

#------------------------------------------------------------------------------
# Zanka for
vsota = 0
for i in range(1, 20, 2):
    print(i)
    vsota += i
print(vsota)

# range vrne generator zaporedja celih števil
# range(5)        -> [0, 1, 2, 3, 4]
# range(1, 5)     -> [1, 2, 3, 4]
# range(1, 5, 2)  -> [1, 3]
# range(5, 0, -2) -> [5, 3, 1]

# Zanka preko elementov niza, seznama, terke itd.
niz = "Teorija"
for znak in niz:
    print(znak)

# Indeksi, prekinitev zanke, razpakiranje v zanki
# niz = "Te" # za preizkus else 
for i, znak in enumerate(niz):
    print(i, znak)
    if i >= 2:
        break
else:
    print("Niz je ocitno krajši od 3 znakov.")

###############################################################################
# Uporaba zunanjih modulov
###############################################################################
# npr.: math, cmath, random, statistics, decimal, numpy, scipy
# Nekaj primerov uvoza:
#   - import math                uvozi modul math, vsi njegovi elementi so v
#                                imenskem prostoru 'math'. Primer: math.sin 
#   - import math as mata        uvoženi elementi v imenskem prostoru 'mata'
#   - from math import *         uvoz se zgodi v globalni imenski prostor seje
#   - from math import sin, pi   uvoz samo naštetih elementov v glob. imen. p.
#   - from math import pi as PI  uvoz v glob. imen. p. z drugim imenom

# Vsebina imenskega prostora s funkcijo dir()
dir()
from math import log10
dir()
import math
dir(math)
math.sin(math.pi/2)

from math import nan, sin, pi, log2, log10
sin(pi/2)

###############################################################################
# Funkcije
###############################################################################
def lastna_informacija(verjetnost, osnova=2):
    """ Izračun lastne informacije glede na verjetnost dogodka 
    lastna_informacija(verjetnost, osnova=2)
    verjetnost - verjetnost dogodka
    osnova     - številska osnova logaritma
    I = - log_osnova(verjetnost)
    """
    if osnova == 2:
        I = -log2(verjetnost)
    elif osnova == 10:
        I = -log10(verjetnost)
    else: 
        I = nan  # nan = NaN = NAN = not a number
    return I

# Klic funkcije
# Pozicijsko posredovanje argumentov, uporaba privzete vrednosti 2 za "osnova"
lastna_informacija(0.5)
# Podani vsi argumenti v zahtevanem vrstnem redu
lastna_informacija(0.5, 2)
# Argumenti podani z imenom (lahko poljuben vrstni red)
lastna_informacija(verjetnost = 0.5, osnova = 10)

###############################################################################
# Sestavljene (vdelane) podatkovne strukture
###############################################################################
#   - Niz     (tip str, nespremenljivi elementi)
#   - Seznam  (tip list)
#   - Terka   (tip tuple, nespremenljivi elementi)
#   - Slovar  (tip dict)
#   - Množica (tip set)
#
# Te strukture so med seboj usklajene: 
#   - indeksiramo jih na enak način
#   - z zanko for gremo preko elementov na enak način
#   - imena metod za delo z njimi so enaka

#------------------------------------------------------------------------------
# Seznam (list)
# Elementi seznama so objekti poljubnega tipa
seznam = [None, True, 42, 3.14, "TIS", lastna_informacija]

# Pisanje elementov v več vrstic (za zadnjim elementom je lahko vejica)
s = [
    "Sofija", "Lenart",
    "Patrik", "Erazem",
]

stevilo = len(s)

# Indeksiranje
prvi = s[0]      # začnemo z 0
tretji = s[2]
zadnji = s[-1]   # indeksiranje od zadaj; -1 pomeni "prvi od zadaj"

# Rezanje
# Pravila podobna kot pri range()
# Za lažje razumevanje si lahko indekse predstavljamo kot mesta rezanja
# 0       1        2        3        4
# |       |        |        |        |
#  Sofija   Lenart   Patrik   Erazem
# |       |        |        |              
# -4      -3       -2       -1
prva_dva = s[0:2]
# Indeks prvega (0) lahko izpustimo
prva_dva = s[:2]
zadnja_dva = s[2:4]
# Indeks zadnjega lahko tudi izpustimo
zadnja_dva = s[2:]
srednja_dva = s[1:3]
srednja_dva = s[1:-1]
# Zadnja dva elementa, ne glede na dolžino seznama
zadnja_dva = s[-2:]
# Brezveze? Tako dobimo kopijo. Kaj pa, če bi napisali vsi = s ?
vsi = s[:]
# Seštevanje seznamov? Lepljenje.
vsi = s[0:2] + s[2:4]
# K rezanju dodajmo korak
lihi = s[0:4:2]
# Prvi in zadnji indeks lahko izpustimo
lihi = s[::2]
# Negativen korak, obrnemo seznam
obrnjeno = s[::-1]

# Operacije na seznamih
#   - spreminjanje
s[0] = "Zofija"
s[1:3] = ["Leonhard", "Lan"]
#   - dodajanje
s.append("Elizabeta")    # Dodajanje na konec
s.insert(1,"Žan")        # Vstavljanje vmes
s.extend(["Jan", "Lan"]) # Razširjanje seznama s seznamom
s += ["Boris", "Alen", "Josip"]   # Isto kot extend
#   - brisanje
del s[2] 
s[4:6] = []        # Tudi tako lahko brišemo 
zadnji = s.pop()   # Brisanje zadnjega in vračanje njegove vrednosti
zadnji = s.pop(-1) # Brisanje zadnjega in vračanje njegove vrednosti
prvi = s.pop(0)    # Brisanje prvega in vračanje njegove vrednosti
s.remove("Erazem") # Brisanje, če ne poznamo indeksa
#   - preverjanje, ali je element v seznamu
print("Lan" in s)
print("Erazem" in s)
#   - prva pojavitev elementa
kje = s.index("Lan")
koliko = s.count("Lan")
#   - urejanje
print(s)
s.sort()             # Uredimo po abecedi, naraščajoče
print(s)
s.sort(reverse=True) # Padajoče
print(s)
s.sort(key=len)      # Podamo kriterij za urejanje (cenilko)
print(s)
#   - obračanje na mestu
s.reverse()
print(s)

# Kopiranje ali ne? Je k kopija s-ja?
k = s 
print(s)
k[0] = "Mirko"
print(s)
# Na seznam kažeta dve imeni: s in k
# Bi radi kopijo? 
k = s[:]
# ali 
k = s.copy()
k[0] = "Tine"
print(s)

#------------------------------------------------------------------------------
# Terka (tuple)
# Terke so seznami, ki jih ne moremo/smemo spreminjati.
# Terke so prostorsko učinkovitejše od seznamov.
terka0 = ()            # Prazna terka
ni_terka = ("Sofija")  # To ni terka, ampak niz
terka1 = ("Sofija", )  # To je terka
terka1 = "Sofija",     # Oklepaje lahko izpuščamo
# terka1[0] = "Zofija"   # Tega ne smemo!
terka2 = ("Sofija", "Lenart", "Sofija")
terka3 = tuple("Sofija") # Pretvorba v terko, razstavljanje po elementih (črkah)
terka4 = tuple([1, 2, 3])
dolzina = len(terka2)
kje = terka2.index("Sofija")
koliko = terka2.count("Sofija")

#------------------------------------------------------------------------------
# Niz (str)
# Lahko jih indeksiramo in režemo kot sezname
# So nespremenljivi (vsebine ne moremo spreminjati)

# Množenje (razmnoževanje) in seštevanje (lepljenje) nizov
krik = "A" + "a"*7 + "!"*3

# "Dodajanje" na konec ali začetek - ne gre za "append", 
# ampak se naredi nov objekt
ime = "Bar"
ime += "bara"  
ime = "Draga " + ime

# Uporabne metode in funkcije
dolzina = len(krik)  
ime2 = ime.upper()       # Spreminjanje v velike črke
ime3 = ime.lower()       # Spreminjanje v male črke
print(ime2.count("BAR")) # Štetje ponovitev
print(ime2.index("BAR")) # iskanje podniza
is1 = "ABC123".isalpha() # Ali je niz sestavljen iz samih črk?
is2 = "ABC123".isalnum() # Ali je niz sestavljen iz črk ali števil?
kosi = ime.split()       # Razbijanje po presledkih
kosi = ime.split("a")    # Razbijanje po "a"
print(", ".join(s)) # Združevanje seznama nizov v enega z ločilom

# Oblikovanje nizov
# Metoda format()
print("Kolega {} ima {} cimrov.".format("Janko", 5))
print("Kolega {} ima {} cimre.".format(k[0], len(s)))
print("Kolega {0} ima {1} cimre. Srečno, {0}!".format(k[0], len(s)))
print("Kolega {ime} ima {n} cimre. Srečno, {ime}!".format(ime=k[0], n=len(s)))
print("Kolega {ime} ima {n:.2f} cimre. Srečno, {ime}!".format(ime=k[0], n=len(s)))

# f-niz
ime = "Erik"
n = 6
print(f"Kolega {ime.upper()} ima {n:.2f} cimrov. Srečno, {ime}!")

#------------------------------------------------------------------------------
# Slovar oz. asociativno polje (dict)
# Elementi imajo svoje unikatne ključe
# Slovar ni urejen, elementi niso zloženi po vrstnem redu dodajanja.
# Slovar je implementiran kot razpršena tabela.
# Ključi morajo biti unikatni in nespremenljivega tipa (števila, nizi, terke)
starost = {"Sofija": 5, "Lenart": 3, "Patrik": 2, "Erazem": None}
# Indeksiramo, spreminjamo in brišemo s ključi
print(starost["Lenart"])
del starost["Erazem"]
# Prirejanje ključu, ki še ne obstaja, pomeni dodajanje v slovar
starost["Erazem"] = 0
# Ključe dobimo s keys()
print(starost.keys())
# Vrednosti dobimo z values()
print(starost.values())
# Pare (terke) ključ, vrednost dobimo z items()
print(starost.items())
# Sprehod preko slovarja z zanko for
for k, v in starost.items():
    print(f"{k} ima {v} let")

#------------------------------------------------------------------------------
# Množica (set)
# V množici so lahko samo nepodvojene (unikatne) vrednosti - tako kot pri matematiki.
# Množica je tako kot slovar implementirana z razpršeno tabelo.
# V množici so lahko samo nespremenljivi elementi (seznam odpade). 
# Elementi v množici so neurejeni (neodvisni od vrstnega reda dodajanja).
# Zapišemo jo z zavitimi oklepaji (kot slovar) z razliko, da tu ni ključev
m1 = {"a", "b", "c"}
# Ali pokličemo konstruktor razreda set(), pri čemer so elementi podani v nizu, terki, seznamu, slovarju, obsegu (range) ...
m2 = set(["a", "b", "c"])
m3 = set(range(1, 20, 2))
# Prazna množica
m0 = set() 
# Dodajanje elementov
m0.add("a")
# Če dodamo element, ki že obstaja, se ne zgodi nič
m0.add("a")
# Brisanje elementov
m0.remove("a")
# Brisanje brez opozorila, če dotični element ne obstaja
m0.discard("a")
# Ali množica vsebuje element
aliVsebuje = "a" in m0 # vrne False

# Matematične operacije nad množicami, ki jih lahko zapišemo z istimi 
# znaki kot bitne ali aritmetične operatorje: 
# union (|), intersection (&), difference (-), symetric_difference (^), issubset (<), ...
a = {1, 2, 3}
b = {2, 3, 4}
unija = a | b  # ali a.union(b)
presek = a & b # ali a.intersection(b)
razlika = a - b
sim_razlika = a.symmetric_difference(b) # ali a ^ b
niPodmnožica = a < b # vrne False
jePodmnožica = {1, 2} < a # vrne True
