import random 
thechosen=input("Zadaj kolkimi kockami chces hodit(maximalne do 10):")
kocky=0
try:
    thechosen=int(thechosen)
    if 1 <= thechosen <= 10:
            while kocky < thechosen:
                   kocka = random.randint(1, 6)
                   print("You rolled:", kocka)
                   kocky = kocky + 1
    else:
            print("Zadal si take cislo s ktorim neviem pracovat!")
except ValueError:
    print("Zadal si to zle!")