from collections import Counter
from math import log2

def naloga1(besedilo: str, p: int) -> float:
    """ Izracun povprecne nedolocenosti na znak 

    Parameters
    ----------
    besedilo : str
        Vhodni niz
    p : int
        Stevilo poznanih predhodnih znakov: 0, 1 ali 2.
        p = 0: H(X1)
            racunamo povprecno informacijo na znak abecede 
            brez poznanih predhodnih znakov
        p = 1: H(X2|X1)
            racunamo povprecno informacijo na znak abecede 
            pri enem poznanem predhodnemu znaku. V bitih.
        p = 2: H(X3|X1,X2)

    Returns
    -------
    H : float 
        Povprecna informacija na znak abecede z upostevanjem 
        stevila poznanih predhodnih znakov 'p'. V bitih.
    """

    abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Odstranimo znake, ki niso črke angleške abecede
    cista_beseda = ''.join(filter(lambda x: x.isalpha(), besedilo))
    
    # Pretvorimo vse črke v velike črke
    cista_beseda = cista_beseda.upper()
    # print("Cista beseda: ", cista_beseda) # testni print

    if (p == 0):
        # Slovar: (črka: stPojavitev)
        slovarCrk = Counter(cista_beseda) 
        # print("Posamezne črke: ", slovarCrk)

        # Izračun entropije: H = -sum(pi*log2pi)
        H = -sum((pi / len(cista_beseda) * log2(pi / len(cista_beseda)) for pi in slovarCrk.values()))
        # print("H: ", H)


    elif (p == 1):
        pari = list(zip(cista_beseda[0:-1], cista_beseda[1:])) # Pridobim vse pare črk - zaporedja 2 črk
        # print(pari)
        # Slovar: (črka/pari: stPojavitev)
        slovarParov = Counter(pari) # Potrebujem frekvence vseh parov črk
        slovarCrk = Counter(cista_beseda) # In vseh posameznih črk
        # print("Vsi pari: ", slovarParov) 
        # print("Posamezne črke: ", slovarCrk)

        # Izračun entropije: H = H1(X1,X2,...,Xn) - H2(X1,X2,...,Xn-1) -> H(x2|x1) = H(x1,x2) - H(x1)
        # Število vseh parov: število znakov v besedi - 1
        H1 = -sum((pi / (len(cista_beseda) - 1) * log2(pi / (len(cista_beseda) - 1)) for pi in slovarParov.values()))
        H2 = -sum((pi / len(cista_beseda) * log2(pi / len(cista_beseda)) for pi in slovarCrk.values())) 
        # print("H1: ", H1)
        # print("H2: ", H2)
        H = H1 - H2


    elif (p == 2):
        pari = list(zip(cista_beseda[0:-1], cista_beseda[1:])) # Pridobim vse pare črk - zaporedja 2 črk
        trojke = [cista_beseda[i:i+3] for i in range(len(cista_beseda)-2)] # Pridobim vse trojke črk - zaporedja 3 črk
        # print(trojke)
        # print(pari)

        # Slovar: (pari/trojke: stPojavitev)
        slovarParov = Counter(pari) # Potrebujem frekvence vseh parov črk
        slovarTrojk = Counter(trojke) # In vseh trojčkov
        # print("Vsi pari: ", slovarParov) 
        # print("Vse trojke: ", slovarTrojk)

        # Izračun entropije: -> H(x3|x1,x2) = H(x1,x2,x3) - H(x1,x2)
        # Število vseh trojk: število znakov v besedi - 2
        H1 = -sum((pi / (len(cista_beseda) - 2) * log2(pi / (len(cista_beseda) - 2)) for pi in slovarTrojk.values()))
        H2 = -sum((pi / (len(cista_beseda) - 1) * log2(pi / (len(cista_beseda) - 1)) for pi in slovarParov.values()))
        # print("H1: ", H1)
        # print("H2: ", H2)
        H = H1 - H2


    elif (p == 3):
        trojke = [cista_beseda[i:i+3] for i in range(len(cista_beseda)-2)] # Pridobim vse trojke črk - zaporedja 3 črk
        cetvorcki = [cista_beseda[i:i+4] for i in range(len(cista_beseda)-3)] # Pridobim vse cetvorcke črk - zaporedja 4 črk
        # print(trojke)
        # print(cetvorcki)

        # Slovar: (trojke/četvorčki: stPojavitev)
        slovarTrojk = Counter(trojke) # Potrebujem frekvence vseh trojčkov črk
        slovarStiric = Counter(cetvorcki) # In vseh četvorčkov
        # print("Vse trojke: ", slovarTrojk) 
        # print("Vsi četvorčki: ", slovarStiric)

        # Izračun entropije: -> H(x4|x1,x2,x3) = H(x1,x2,x3,x4) - H(x1,x2,x3)
        # Število vseh četvorčkov: število znakov v besedi - 3
        H1 = -sum((pi / (len(cista_beseda) - 3) * log2(pi / (len(cista_beseda) - 3)) for pi in slovarStiric.values()))
        H2 = -sum((pi / (len(cista_beseda) - 2) * log2(pi / (len(cista_beseda) - 2)) for pi in slovarTrojk.values()))
        # print("H1: ", H1)
        # print("H2: ", H2)
        H = H1 - H2

    return H


# Primer uporabe funkcije
"""
besedilo = 'Danes bom naredil 1. domaco nalogo!'
test = 'AbB,a.bC'
izpis = naloga1(test, 2)
print(izpis)
"""
