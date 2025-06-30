import numpy as np
from PIL import Image
from math import pi
import matplotlib.pyplot as plt

"""
def izdelaj_sliko():
    # Ustvarimo 16x16 sliko z naključnimi vrednostmi
    np.random.seed(0)  # Za reproducibilnost
    slika = np.random.randint(0, 256, (8, 8), dtype=np.uint8)

    # Izris slike
    plt.imshow(slika, cmap='gray', vmin=0, vmax=255)
    plt.title("test2")
    plt.axis('off')
    plt.show()

    # Shranimo sliko za uporabo
    plt.imsave("./primeri/slike/test2.png", slika, cmap='gray')
"""

def calculate_psnr(slika, slikaOut_Output): 
    assert slika.shape == slikaOut_Output.shape, "Sliki morata imeti enake dimenzije."
    # Velikost slike
    H, W = slika.shape
    # Maksimalna vrednost piksla za 8-bitne slike
    MAX_I = 2**8 - 1
    # MSE (Mean Squared Error)
    mse = np.mean((slika - slikaOut_Output) ** 2)
    # Preveri, če je MSE enak nič (izognemo se deljenju z nič)
    if mse == 0:
        return float('inf')
    # Izračunaj PSNR
    psnr = 20 * np.log10(MAX_I) - 10 * np.log10(mse)
    return psnr

def poenostavi_sliko(slika: np.array, velikostOkna: int) -> np.array:
    # Premik vrednosti na interval [-128, 127]
    slika_P = slika - 128
    #print("\nPremik slike:\n", slika_P)

    # Nastavimo N in k
    N=velikostOkna
    k=np.array(range(0,N))

    # Vrstični DCT 
    # Rezerviramo in inicaliziramo prostor za izhodno sliko
    slikaOut_I = np.zeros(slika.shape)

    for col in range(N):
        for row in range(N):
            slikaOut_I[row, col]=2*np.sum(slika_P[row,:]*np.cos(pi/N*(k+1/2)*col))
    #print("\nVrsticni DCT:\n", slikaOut_I)

    # Stolpični DCT
    slikaOut_P = np.zeros(slika.shape)
    for col in range(N):
        for row in range(N):
            slikaOut_P[row, col]=2*np.sum(slikaOut_I[:,col]*np.cos(pi/N*(k+1/2)*row))
    #print("\nStolpicni DCT:\n", slikaOut_P)

    # Kvantizacija
    slikaOut_P2 = np.zeros(slika.shape)
    for col in range(N):
        for row in range(N):
            # Kvantizacijski faktor Q
            Q=20*N*(1+row+col)
            slikaOut_P2[row, col]=np.sign(slikaOut_P[row, col])*np.floor(np.abs(slikaOut_P[row, col])/Q)*Q

    # Rezultat za vse piksle po kvantizaciji
    #print("\nKvantizacija:\n", slikaOut_P2)

    # Stolpični IDCT
    n=np.array(range(1,N))
    slikaOut_I2 = np.zeros(slika.shape)
    for row in range(N):
        for column in range(N):
            X0=slikaOut_P2[0,column]
            slikaOut_I2[row, column]=1/N*(X0/2+np.sum(slikaOut_P2[1:,column]*np.cos(pi/N*(row+1/2)*n)))
    #print("\nStolpični IDCT:\n", slikaOut_I2)

    # Vrstični IDCT za piksel (2,1)
    slikaOut_P2 = np.zeros(slika.shape)
    for row in range(N):
        for col in range(N):
            X0=slikaOut_I2[row,0]
            slikaOut_P2[row, col]=1/N*(X0/2+np.sum(slikaOut_I2[row,1:]*np.cos(pi/N*(col+1/2)*n)))

    # Rezultat za celotno sliko po IDCT
    #print("\nVrstični IDCT:\n", slikaOut_P2)

    # Piksle zaokrožimo navzdol, prištejemo 128 in omejimo na interval [0,255]
    slikaOut_Output = np.zeros(slika.shape)
    for row in range(N):
        for col in range(N):
            slikaOut_Output[row, col]=min(max(np.floor(slikaOut_P2[row, col])+128, 0), 255)
    #print("\nKoncni rezultat:\n", slikaOut_Output)

    return slikaOut_Output


def naloga4(slika: np.array, velikostOkna: int) -> float:
    #######################################
    # Preberemo sliko in jo pretvorimo v sivinsko sliko
    # pot_do_slike = "./primeri/" + pot
    # slika_file = Image.open(pot_do_slike).convert('L')  # read as grayscale
    # slika = np.array(slika_file, dtype=np.int16)

    #print("\nVhodna slika:\n", slika)

    H, W = slika.shape
    poenostavljena_slika = np.zeros((H, W), dtype=np.int16)

    for i in range(0, H, velikostOkna):
        for j in range(0, W, velikostOkna):
            blok = slika[i:i + velikostOkna, j:j + velikostOkna]
            #print("\nBlok:\n", blok)
            if blok.shape[0] == velikostOkna and blok.shape[1] == velikostOkna:
                obdelan_blok = poenostavi_sliko(blok, velikostOkna)
                poenostavljena_slika[i:i + velikostOkna, j:j + velikostOkna] = obdelan_blok
            #print("\n----------------------------------------------------------------------------------------------------------------------------\n")
            #print("----------------------------------------------------------------------------------------------------------------------------\n")

    # PSNR
    #print("\nIzhodna slika:\n", poenostavljena_slika)
    PSNR = calculate_psnr(slika, poenostavljena_slika)
    # print("\nPSNR: ", PSNR, "\n")

    return PSNR

# izdelaj_sliko()
# naloga4("slike/2.png", 8)
