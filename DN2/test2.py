def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    """
    Izvedemo kodiranje ali dekodiranje z algoritmom LZW.
    Zacetni slovar vsebuje vse 8-bitne vrednosti (0-255).
    Najvecja dolzina slovarja je 4096.
    
    Parameters
    ----------
    vhod : list or str
        Seznam vhodnih znakov (ko nacin=0) ali besedilo (ko nacin=1).
    nacin : int
        Stevilo, ki doloca nacin delovanja:
        0: kodiramo ali
        1: dekodiramo.
        
    Returns
    -------
    (izhod, R) : tuple[list, float]
        izhod : list
            Ce je nacin = 0: "izhod" je kodiran "vhod".
            Ce je nacin = 1: "izhod" je dekodiran "vhod".
        R : float
            Kompresijsko razmerje.
    """
    
    def inicializiraj_slovar():
        """
        Inicializira slovar z vsemi 8-bitnimi vrednostmi (0-255).
        """
        slovar = {}
        for i in range(256):
            slovar[bytes([i])] = i
        return slovar
    
    def kodiraj(vhod):
        """
        Izvede kodiranje vhoda z algoritmom LZW.
        """
        slovar = inicializiraj_slovar()
        izhod = []
        N = b''
        for znak in vhod:
            NZ = N + bytes([znak])
            if NZ in slovar:
                N = NZ
            else:
                izhod.append(slovar[N])
                slovar[NZ] = len(slovar)
                N = bytes([znak])
        if N:
            izhod.append(slovar[N])
        return izhod
    
    def dekodiraj(vhod):
        """
        Izvede dekodiranje vhoda z algoritmom LZW.
        """
        slovar = inicializiraj_slovar()
        izhod = bytearray()
        K = vhod.pop(0)
        izhod.extend(bytes([K]))
        for k in vhod:
            if k in slovar:
                znak = slovar[k]
            elif k == len(slovar):
                znak = bytes([K[0]])
            else:
                raise ValueError('Napaka pri dekodiranju.')
            izhod.extend(znak)
            slovar[len(slovar)] = bytes([K[0]]) + bytes([znak[0]])
            K = k
        return izhod
    
    # Izvajanje kodiranja ali dekodiranja glede na nacin
    if nacin == 0:
        izhod = kodiraj(vhod)
        R = (len(izhod) * 12) / (len(vhod) * 8)
    elif nacin == 1:
        izhod = dekodiraj(vhod)
        R = (len(izhod) * 12) / (len(vhod) * 8)
    else:
        raise ValueError("Neveljaven nacin. Nacin mora biti 0 (za kodiranje) ali 1 (za dekodiranje).")
    
    return izhod, R

# Primer uporabe funkcije
# vhod = [66, 82, 256, 82, 259, 82]  # Besedilo vhodnega sporočila
vhod = "BRBRRRRR"
nacin = 0  # 0 za kodiranje, 1 za dekodiranje
izhod, R = naloga2(vhod, nacin)
print("Izhod:", izhod)
print("Kompresijsko razmerje:", R)
