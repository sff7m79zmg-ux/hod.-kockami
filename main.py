import random 
thechosen=input("Zadaj kolkimi kockami chces hodit:")
try:
    thechosen=int(thechosen)
    if thechosen == 1:
            kocka1 = random.randint(1,6)
            print("1. kocka:", kocka1)
    elif thechosen == 2:
            kocka1 = random.randint(1,6)
            kocka2 = random.randint(1,6)
            print("1. kocka:", kocka1)
            print("2. kocka:", kocka2)
    elif thechosen == 3:
            kocka1 = random.randint(1,6)
            kocka2 = random.randint(1,6)
            kocka3 = random.randint(1,6)
            print("1. kocka:", kocka1)
            print("2. kocka:", kocka2)
            print("3. kocka:", kocka3)
    else:
            print("Zadal si take cislo s ktorim neviem pracovat!")
except ValueError:
    print("Zadal si to zle!")