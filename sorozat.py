import random
veletlen_szam = []

def veletlen_szamok():
    for i in range(0, 8,1):
        veletlen_szam = []
        szam: int = random.randint(-100, 859)
        veletlen_szam.append(str(szam))
        if i < 7:
            print(szam, end = ";")
        else:
            print(szam, end = " ")
    
def tizzel_oszthatoak_szama(veletlen_szam):
    tizzel_oszthatoak: int = 0
    for i in range(0, len(veletlen_szam), 1):
        if veletlen_szam[i] % 10 == 0:
            tizzel_oszthatoak += 1
        
    return tizzel_oszthatoak