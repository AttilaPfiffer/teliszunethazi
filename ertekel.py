def feladat1():
    napok: str = str(input("Adja meg a hét napját: "))
    ora_nev: str = str(input("Adja meg az óra nevét: "))
    ertekeles: int = int(input("Adja meg az értékelést (0 - 5): "))

    if 0 <= ertekeles <= 5:
        print("Köszönjük az értékelést!")
        print(f"Hét napja: {napok} \nÓra neve: {ora_nev} \nÉrtékelés: {ertekeles}")
    elif ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható!")

