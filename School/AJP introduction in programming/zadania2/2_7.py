# 7.	Sprawdzenie czy liczba podana przez użytkownika jest pierwsza.

import math  # importujemy biblioteke potrzebna do pierwiastkowania


user_number = int(input("Podaj liczbę naturalną, dla której zostanie sprawdzony warunek czy podana liczba jest liczbą pierwszą: "))
if user_number < 2:
    print(f"Podana przez Ciebie liczba jest nieodpowiednia. Proszę odpalić na nowo program oraz podać inną liczbę.")
else:
    list_of_numbers = [True] * (user_number + 1)
    # print(list_of_numbers)  # sprawdzenie utworzonej tablicy
    for i in range(2, (int(math.sqrt(user_number)))+1):
        if list_of_numbers[i]:
            for k in range(i * i, user_number + 1, i):
                list_of_numbers[k] = False
    # print(list_of_numbers)  # sprawdzenie algorytmu - sito eratostenesa
    if list_of_numbers[user_number] == True:
        print(f"Podana przez Ciebie liczba '{user_number}' jest liczbą pierwszą!")
    else:
        print(f"Podana przez Ciebie liczba '{user_number}' nie jest liczbą pierwszą!")
