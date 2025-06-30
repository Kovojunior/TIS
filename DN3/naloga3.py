import math
import numpy as np

# Vrne paritetni bit vhoda
def calculate_parity(y):
    count_ones = sum(y)  # Seštejemo vse enice v vektorju y
    parity = count_ones % 2  # Izračunamo paritetni bit
    return parity

# Preveri, ali je vektor ničelen
def is_zero_vector(s):
    return all(element == 0 for element in s)


# Vrne DATA bite izhodnega vektorja y
def get_data_bits(y, n):
    return y[:n]


# Vrne seštevek vektorjev y in e po modulu 2
def sestej_vektorja(y, e):
    # Seštejemo vektorja y in e po modulu 2
    y2 = [(yi + ei) % 2 for yi, ei in zip(y, e)]
    return y2


# Izračuna vektor napake in ga vrne
def find_error_vector(s, n, H):
    # Pretvorimo vektor s in matriko H v numpy array za enostavnejše delo
    s_array = np.array(s)
    H_array = np.array(H)

    # Poiščemo indeks stolpca v matriki H, katerega stolpec je enak vektorju s
    column_index = np.where((H_array.T == s_array).all(axis=1))[0][0]

    # Zgradimo vektor e z ničlami, razen na indeksu column_index, kjer je 1
    e = [0] * n
    e[column_index] = 1
    return e


# Množi vektor y z matriko H transponirano po modulu 2 in vrne dobljeni vektor s, ki predstavlja sindrom
def return_sindrom(y, H):
    # Pretvorimo y v numpy array za enostavnejše računanje
    y_array = np.array(y)

    # Pomnožimo y z transponirano matriko H po modulu 2
    s_array = np.dot(y_array, H.T) % 2

    # Pretvorimo rezultat nazaj v seznam
    s = list(s_array)
    return s


# Odstrani zadnji element iz seznama y in vrne nov seznam
def clip_y(y):
    return y[:-1]


# Zgradi matriko H po navodilih
def build_H(n):
    # Dolžina binarnega zapisa števila n
    m = int(np.ceil(np.log2(n)))

    H_prime = np.zeros((m, n), dtype=int)
    for i in range(1, n + 1):
        binary = bin(i)[2:]  # Pretvorimo i v dvojiški zapis
        binary = binary.zfill(m)  # Dopolnimo z ničlami na začetku
        # print("binary: ", binary) # to še dobro deluje
        for j in range(len(binary)):
            H_prime[j][i - 1] = int(binary[j])  # Nastavimo vrednosti v H'
            # print("h' vrednost: ", int(binary[j]))
    # print(H_prime)

    # Ustvarimo matriko H
    H = np.zeros((m, n), dtype=int)
    col_idx = 0
    for j in range(n):
        if j + 1 not in [2**k for k in range(m)]:  # Preverimo ali je število potenca števila 2
            H[:, col_idx] = H_prime[:, j]  # Kopiramo stolpec v H
            col_idx += 1

    col_idx = n - m  # Nastavimo indeks stolpca za potenčna števila 2
    for j in range(n):
        if j + 1 in [2**k for k in range(m)]:
            H[:, col_idx] = np.flip(H_prime[:, j])
            col_idx += 1

    return H


# Vrne število podatkovnih DATA bitov v vektorju Y
def num_data_bits(n):
    return math.ceil(math.log2(n)) + 1


def naloga3(vhod: list, n: int) -> tuple[list, str]:
    """
    Izvedemo dekodiranje binarnega niza `vhod`, zakodiranega 
    z razsirjenim Hammingovim kodom dolzine `n` in poslanega 
    po zasumljenem kanalu.
    Nad `vhod` izracunamo vrednost `crc` po standardu CRC-8/CDMA2000.

    Parameters
    ----------
    vhod : list
        Sporocilo y, predstavljeno kot seznam bitov (stevil tipa int) 
    n : int
        Stevilo bitov v kodni zamenjavi
    
    Returns
    -------
    (izhod, crc) : tuple[list, str]
        izhod : list
            Odkodirano sporocilo y (seznam bitov - stevil tipa int)
        crc : str
            Vrednost CRC, izracunana nad `vhod`. Niz dveh znakov.
    """

    # n = 8
    # vhod = [1, 0, 0, 1, 1, 1, 0, 1]

    n_h = n - 1
    H = build_H(n_h)
    # print("Matrika H za (n-1) =", n_h, "je:")
    # print(H)

    p = calculate_parity(vhod)
    # print("Paritetni bit: ", p)

    y2 = clip_y(vhod)
    # print("Vhod: ", vhod, ", Clipped vhod y2 = ", y2)
    # print("Vhodni vektor: ", vhod)
    # print("Vektor y = ", y2)

    s = return_sindrom(y2, H)
    # print("Sindrom s = ", s)

    k = num_data_bits(n_h)
    # print("K: ", k)

    # Ni napake, napaka na paritetnem bitu ali dvojna napaka -> izšluščimo podatkovne bite
    if ((p == 0 and is_zero_vector(s)) or (p == 0 and not is_zero_vector(s)) or (p == 1 and is_zero_vector(s))):
        izhod = get_data_bits(vhod, k)
        #print("Z brez popravljanja: ", izhod)

    # Enojna napaka -> Popravimo in izluščimo podatkovne bite
    elif(p == 1 and not is_zero_vector(s)):
        e = find_error_vector(s, n_h, H)
        #print("Error vector: ", e)

        y_izhod = sestej_vektorja(y2, e)
        #print("Popravljeni y: ", y_izhod)

        izhod = get_data_bits(y_izhod, k)
        #print("Z s popravljanjem: ", izhod)

    crc = ''
    return (izhod, crc)
    