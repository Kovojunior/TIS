# Napolni začetni slovar z ASCII znaki do 256
def napolni_slovar():
    slovar = {}
    for i in range(256):
        slovar[chr(i)] = i
    return slovar


# Kodiranje vhoda
def kodiranje(vhod):
    kodirni_slovar = napolni_slovar()  # Začetni slovar znakov z ASCII vrednostmi
    kodirano_sporocilo = []  # Seznam za shranjevanje kodiranih zamenjav
    
    N = ''  # Začetni prazen niz
    for znak in vhod:
        NZ = N + znak  # Naredimo novo zaporedje z znakom z
        if NZ in kodirni_slovar:
            N = NZ  # Če je že v slovarju, nadaljujemo z gradnjo zaporedja
        else:
            kodirano_sporocilo.append(kodirni_slovar[N])  # Dodamo kodno zamenjavo za niz N
            if len(kodirni_slovar) < 4096:  # Preverimo, če je število vnosov v slovarju manjše od 4096
                kodirni_slovar[NZ] = len(kodirni_slovar)  # Dodamo novo zaporedje v slovar
            N = znak  # Začnemo graditi novo zaporedje z novim znakom
    
    # Dodamo kodno zamenjavo za zadnji znak ali zaporedje
    if N:
        kodirano_sporocilo.append(kodirni_slovar[N])
    
    return kodirano_sporocilo


# Dekodiranje vhoda
def dekodiranje(kodirano):
    dekodirni_slovar = {i: chr(i) for i in range(256)}  # Začetni slovar znakov z ASCII vrednostmi
    dekodirano_sporocilo = []  # Seznam za shranjevanje dekodiranega sporočila
    
    K = kodirano.pop(0)  # Preberemo prvo kodno zamenjavo
    dekodirano_sporocilo.append(dekodirni_slovar[K])  # Dodamo prvi znak v dekodirano sporočilo
    
    for k in kodirano:
        if k in dekodirni_slovar:
            N = dekodirni_slovar[k]  # Poiščemo pripadajoči niz v slovarju
        else:
            N = dekodirni_slovar[K] + dekodirni_slovar[K][0]  # Sestavimo novo zaporedje
        dekodirano_sporocilo.extend(N)  # Dodamo dekodirane znake v sporočilo po enega
        if len(dekodirni_slovar) < 4096:  # Preverimo, če je število vnosov v slovarju manjše od 4096
            dekodirni_slovar[len(dekodirni_slovar)] = dekodirni_slovar[K] + N[0]  # Dodamo novo zaporedje v slovar
        K = k  # Nastavimo novo vrednost K za naslednjo iteracijo
    
    return dekodirano_sporocilo


# Izračun kompresijskega razmerja
def izracun_kompresijskega_razmerja(vhod, kodirano):
    dolzina_vhoda = len(vhod) * 8
    dolzina_kodiranega = len(kodirano) * 12
    razmerje = dolzina_vhoda / dolzina_kodiranega
    return razmerje


# Izračun dekompresijskega razmerja
def izracun_dekompresijskega_razmerja(vhod, dekodirano):
    dolzina_vhoda = (len(vhod) + 1) * 12  # + 1 zaradi .pop v funkciji dekodiranja
    dolzina_dekodiranega = len(dekodirano) * 8
    razmerje = dolzina_dekodiranega / dolzina_vhoda
    return razmerje


def naloga2(vhod, nacin):
    """
    Izvedemo kodiranje ali dekodiranje z algoritmom LZW.
    Začetni slovar vsebuje vse 8-bitne vrednosti (0-255).
    Največja dolžina slovarja je 4096.
    Parameters
    ----------
    vhod : list
        Seznam vhodnih znakov: bodisi znaki abecede (ko kodiramo) bodisi kodne zamenjave (ko dekodiramo).
    nacin : int
        Število, ki določa način delovanja:
        0: kodiramo ali
        1: dekodiramo.
    Returns
    -------
    (izhod, R) : tuple [list, float]
        izhod : list
            Če je nacin = 0: "izhod" je kodiran "vhod".
            Če je nacin = 1: "izhod" je dekodiran "vhod".
        R : float
            Kompresijsko razmerje
    """
    if nacin == 0:
        kodirano = kodiranje(vhod)
        R = izracun_kompresijskega_razmerja(vhod, kodirano)
        #print("izhod: ", kodirano)
        #print("kompresijsko razmerje: ", R)
        return kodirano, R
    
    elif nacin == 1:
        dekodirano = dekodiranje(vhod)
        R = izracun_dekompresijskega_razmerja(vhod, dekodirano)
        #print("izhod: ", dekodirano)
        #print("kompresijsko razmerje: ", R)
        return dekodirano, R
    
    # else:
        # raise ValueError('Neveljaven način. Nacin mora biti 0 ali 1.')
    
"""
vhodno_sporocilo_kod = "BRBRRRRR"  # Vhodno sporočilo kodiraj
kodirano = kodiranje(vhodno_sporocilo_kod)
razmerje = izracun_kompresijskega_razmerja(vhodno_sporocilo_kod, kodirano)
print("Kodirano sporočilo:", kodirano)
print("Kompresijsko razmerje: ", razmerje)

vhodno_sporocilo_dekod = [66, 82, 256, 82, 259, 82]  # Vhodno sporočilo dekodiraj
dekodirano = dekodiranje(vhodno_sporocilo_dekod)
razmerje = izracun_dekompresijskega_razmerja(vhodno_sporocilo_dekod, dekodirano)
print("Dekodirano sporočilo:", dekodirano)
print("Dekompresijsko razmerje: ", razmerje)
"""