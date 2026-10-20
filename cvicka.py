import random
print("Vitaj v hre kocky!")
print("Tato hra ma 2 rezimi. 1. rezim je kde mozete hrat klasicke kocky ale mozete vybrat s kolkymi kockami chcete hrat.\n" \
"Tento moznost oznaceny pismenom  K. 2. rezim je kde mozete hodit s kosky s viacerimi opakovaniami. Tento moznost bude oznacena ako V.\n" \
"vzdy mozete vybrat s kolkymi kockami chcete hrat a moznosti su 1, 2, a 3. Pri V tak isto mate moznost vybrat kocky ale tam este mate zadat opakovanie a=500, b= 1 000, c=5 000, a d= 10 000.")
print("Uzivajte si hru")
a=500
b=1000
c=5000
d=10000
rezim=input("Rezim hrania K/V:")
thechosen=input("Zadaj kolkymi kockami chces hodit(maximalne do 3):")
#opakovanie=input("Zadaj kolko krat chces hodit s kockami (vyber jedno pismeno):")
pokracovat=input("Mozeme zacat A/N:")

if rezim=="K" or rezim=="k":
    najvyssi_pocet=0
    najcastejsie_cislo = 0
    vysledky=[]
    hody=0
    if pokracovat=="A" or pokracovat=="a":
        try:
            thechosen=int(thechosen)
            if thechosen == 1:
                    while pokracovat=="A" or pokracovat=="a":
                        kocka1 = random.randint(1, 6)
                        vysledky.append(kocka1)
                        hody=hody+1
                        print("Hodili ste:", kocka1)
                        pokracovat=input("Chces este pokracovat? (A/N):")

                    sucet=sum(vysledky)
                    print("Hody boli:", vysledky)
                    print("Sucet celkovo hodenych kociek:", sucet)  
                    print("Sucet hodov:", hody)
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
            elif thechosen == 2:
                    while pokracovat=="A" or pokracovat=="a":
                        kocka1 =random.randint(1, 6)
                        kocka2 =random.randint(1, 6)
                        vysledky.append((kocka1+kocka2))
                        hody=hody+1
                        print("Hodili ste:", kocka1, kocka2)
                        pokracovat=input("Chces este pokracovat? (A/N):")
                    
                    sucet=sum(vysledky)
                    print("Hody boli:", vysledky)
                    print("Sucet celkovo hodenych kociek:", sucet)
                    print("Sucet hodov:", hody)
                    frekvencia = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
                    for hod in vysledky:
                        frekvencia[hod] = frekvencia[hod] + 1
                    print(frekvencia)

                    for cislo, pocet in frekvencia.items():
                        if pocet > najvyssi_pocet:
                            najvyssi_pocet = pocet
                            najcastejsie_cislo = cislo

                    print(f"Najčastejšie číslo: {najcastejsie_cislo}")
                    print(f"Počet výskytov: {najvyssi_pocet}")
            elif thechosen == 3:
                    while pokracovat=="A" or pokracovat=="a":
                        kocka1 = random.randint(1, 6)
                        kocka2 =random.randint(1, 6)
                        kocka3 = random.randint(1, 6)
                        vysledky.append((kocka1+kocka2+kocka3))
                        hody=hody+1
                        print("Hodili ste:", kocka1, kocka2, kocka3)
                        pokracovat=input("Chces este pokracovat? (A/N):")

                    sucet=sum(vysledky)
                    print("Hody boli:", vysledky)
                    print("Sucet celkovo hodenych kociek:", sucet)
                    print("Sucet hodov:", hody)
                    frekvencia = {3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0}
                    for hod in vysledky:
                        frekvencia[hod] = frekvencia[hod] + 1
                    print(frekvencia)

                    for cislo, pocet in frekvencia.items():
                        if pocet > najvyssi_pocet:
                            najvyssi_pocet = pocet
                            najcastejsie_cislo = cislo

                    print(f"Najčastejšie číslo: {najcastejsie_cislo}")
                    print(f"Počet výskytov: {najvyssi_pocet}")
            else:
                    print("Zadal si take cislo s ktorim neviem pracovat!")
        except ValueError:
            print("Zadal si to zle!")
    else:
        print("Takze nechcete hrat, tak sa majte pekne a dufam ze sa vratite!")