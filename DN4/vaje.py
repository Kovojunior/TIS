import numpy as np
from PIL import Image
from math import pi

# Namestitev vseh paketov
# > pip install numpy pillow

#######################################
# Preberemo sliko
slika_file = Image.open("./primeri/slike/1.png").convert('L') # read as grayscale
slika = np.array(slika_file, dtype=np.int16)

print(slika)
# Rezerviramo in inicaliziramo prostor za izhodno sliko
slikaOut = np.zeros(slika.shape)

# Premik vrednosti na interval [-128, 127]
slika = slika - 128
print(slika)

# Velikost okna je 4x4, kar je enako velikosti slike
# Vrstični DCT za stolpec (:,1)
column=1
N=slika.shape[0]
k=np.array(range(0,4))
for row in range(N):
    slikaOut[row, column]=2*np.sum(slika[row,:]*np.cos(pi/N*(k+1/2)*column))
print(slikaOut)

# Stolpični DCT za piksel (3,1)
row=3
column=1
slikaOut[row, column]=2*np.sum(slikaOut[:,column]*np.cos(pi/N*(k+1/2)*row))
print(slikaOut)

# Kvantizacija za piksel (3,1)
# Kvantizacijski faktor Q
Q=20*N*(1+row+column)
#Kvantizacija
slikaOut[row, column]=np.sign(slikaOut[row, column])*np.floor(np.abs(slikaOut[row, column])/Q)*Q
print(slikaOut)

# Rezultat za vse piksle po kvantizaciji
slikaOut=np.array([[0,0,0,0],[0,-480,0,-1200],[0,0,0,0],[0,-1200,0,-3360]]).astype(float)

# Stolpični IDCT za vrstico (2,:)
n=np.array(range(1,4))
row=2
for column in range(N):
    X0=slikaOut[0,column]
    slikaOut[row, column]=1/N*(X0/2+np.sum(slikaOut[1:,column]*np.cos(pi/N*(row+1/2)*n)))
print(slikaOut)

# Vrstični IDCT za piksel (2,1)
row=2
column=1
X0=slikaOut[row,0]
slikaOut[row, column]=1/N*(X0/2+np.sum(slikaOut[row,1:]*np.cos(pi/N*(column+1/2)*n)))
print(slikaOut)

# Rezultat za celotno sliko po IDCT
# slikaOut=np.array([[-109.4,116.7,-116.7,109.4],[116.7,-130.6,130.6,-116.7],[-116.7,130.6,-130.6,116.7],[109.4,-116.7,116.7,-109.4]]) 

# Piksel (2,1) zaokrožimo navzdol prištejemo 128 in omejimo na interval [0,255]
slikaOut[row, column]=min(max(np.floor(slikaOut[row, column])+128, 0), 255)
print(slikaOut)