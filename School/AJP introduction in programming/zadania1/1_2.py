user_number = float(input("Podaj liczbę: "))
if user_number >= -100 and user_number <= 100:
    if user_number != 50:
        print(f"Podana przez Ciebie liczba '{user_number}' mieści się w przedziale od -100 do 100 i nie jest liczbą 50.")
    else:
        print(f"Podana przez Ciebie liczba '{user_number}' mieści się w przedziale od -100 do 100 i jest liczbą 50.")
else:
    print(f"Podana przez Ciebie liczba '{user_number}' nie mieści się w przedziale od -100 do 100.")