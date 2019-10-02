"""sortowanie liczb
Trzy dowolne liczby zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej.
"""
"""list = []
number1 = int(input("Podaj pierwszą liczbę: "))
list.append(number1)
number2 = int(input("Podaj drugą liczbę: "))
list.append(number2)
number3 = int(input("Podaj trzecią liczbę: "))
list.append(number3)
print("*" * 33)
print(list)
list.sort()
list.reverse()
print("*" * 33)
print("Największa liczba to:", max(list))
print("Poniżej posortowane liczby od największej do najmniejszej:)")
print(list)"""

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
number3 = int(input("Podaj trzecią liczbę: "))

if number1 > number2:
    max = number1
    if number1 > number3:
        max = number1
        if number2 > number3:
            medium = number2
            low = number3
        else:
            low = number2
            medium = number3
    else:
        max = number3
        medium = number1
        low = number2
else:
    max = number2
    if number2 > number3:
        max = number2
        if number1 > number3:
            medium = number1
            low = number3
        else:
            medium = number3
            low = number1
    else:
        max = number3
        medium = number2
        low = number1
"""if number1 > number2 and number1 > number3:
    max = number1
elif number2 > number1 and number2 > number3:
    max = number2
else:
    max = number3"""

print("*" * 30)
print("Największą liczbą jest liczba:", max)
print("KONIEC PROGRAMU MAX.")
print("*" * 30)
print("Poniżej posortowane liczby od największej do najmniejszej:)")
print(max, medium, low)
print("KONIEC PROGRAMU SORT.")