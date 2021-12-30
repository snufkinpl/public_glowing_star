user_number = float(input("Podaj liczbę: "))
if user_number >= 0 and user_number <= 100:
    print(f"Podana przez Ciebie liczba '{user_number}' mieści się w przedziale od 0 do 100.")
else:
    print(f"Podana przez Ciebie liczba '{user_number}' nie mieści się w przedziale od 0 do 100.")