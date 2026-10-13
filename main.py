import random 
thechosen=input("Zadaj kolkimi kockami chces hodit(maximalne do 3):")
kocky=0
vysledky=[]
try:
    thechosen=int(thechosen)
    if 1 <= thechosen <= 3:
            while kocky < thechosen:
                   kocka = random.randint(1, 6)
                   vysledky.append(kocka)
                   print("Hodili ste:", kocka)
                   kocky = kocky + 1

            sucet=sum(vysledky)
            print("Hody boli:", vysledky) 
            print("Sucet hodov:", sucet)
    else:
            print("Zadal si take cislo s ktorim neviem pracovat!")
except ValueError:
    print("Zadal si to zle!")