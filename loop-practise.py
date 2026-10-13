import random


# ORIGINAL IDEA


# repeats = 0
# thechosen = input("Zadaj kolkimi kockami chces hodit (maximum je 10):")

# try:
#     thechosen = int(thechosen)

#     while thechosen <= 10:
#         kocka = random.randint(1, 6)
#         repeats = repeats + 1
#         print("Hodil si:", kocka)

# except ValueError:
#     print("Zadal si to zle!")



# SECOND ATTEMPT


# repeats = 0
# thechosen = input("Zadaj kolkimi kockami chces hodit (maximum je 10):")

# try:
#     thechosen = int(thechosen)

#     while thechosen <= 10:
#         kocka = random.randint(1, 6)
#         repeats = repeats + 1

#         if repeats == thechosen:
#             break

#         print("Hodil si:", kocka)

# except ValueError:
#     print("Zadal si to zle!")



# PRACTICE EXAMPLE: WHILE LOOP

# counter = 0

# while counter < 3:
#     print("Rolling the dice...")
#     counter = counter + 1



# CURRENT WORKING EXERCISE
# Roll one die a chosen number of time

vysledky = []
repeats = 0
thechosen = input("How many times should I roll? ")

try:
    thechosen = int(thechosen)

    while repeats < thechosen:
        kocka = random.randint(1, 6)
        vysledky.append(kocka)
        print("You rolled:", kocka)
        repeats = repeats + 1

    sucet=sum(vysledky)
    print("The rolls were:", vysledky) 
    print("The sum of your rolls is:", sucet)
except ValueError:
    print("You entered an invalid value!")