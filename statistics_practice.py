'''pocet_jednotiek = 0
pocet_dvojok = 0
pocet_trojok=0
pocet_stvorok = 0
pocet_patiek = 0
vysledky = [3, 5, 3, 2, 5, 3]   
for hod in vysledky:
    if hod ==1:
        pocet_jednotiek = pocet_jednotiek + 1
    if hod ==2:
        pocet_dvojok = pocet_dvojok + 1
    if hod ==3:
        pocet_trojok = pocet_trojok + 1
    if hod ==4:
        pocet_stvorok = pocet_stvorok + 1
    if hod ==5:
        pocet_patiek = pocet_patiek + 1
print(f"Počet jednotiek: {pocet_jednotiek}")
print(f"Počet dvojok: {pocet_dvojok}")
print(f"Počet trojok: {pocet_trojok}")
print(f"Počet štvorok: {pocet_stvorok}")
print(f"Počet piatok: {pocet_patiek}")'''

'''frekvencia = {1:0, 2:0, 3:0}

frekvencia[3]=frekvencia[3] + 1
frekvencia[2]=frekvencia[2] + 1
print(frekvencia)'''

'''vysledky = [3, 5, 3, 2, 5, 3]
frekvencia = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for hod in vysledky:
    frekvencia[hod] = frekvencia[hod] + 1
print(frekvencia)'''


najvyssi_pocet = 0
najcastejsie_cislo = 0
vysledky = [3, 5, 3, 2, 5, 3]
frekvencia = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for hod in vysledky:
    frekvencia[hod] = frekvencia[hod] + 1
print(frekvencia)

for cislo, pocet in frekvencia.items():
    if pocet > najvyssi_pocet:
        najvyssi_pocet = pocet
        najcastejsie_cislo = cislo

print(f"Najčastejšie číslo: {najcastejsie_cislo}")
print(f"Počet výskytov: {najvyssi_pocet}")