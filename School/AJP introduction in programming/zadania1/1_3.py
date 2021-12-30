user_number1 = int(input("Podaj liczbę 1: "))
user_number2 = int(input("Podaj liczbę 2: "))

if user_number1 > user_number2:
    print(f"Wynik dodawania dwóch liczb: '{user_number1}' oraz '{user_number2}' = {user_number1 + user_number2}")
    print(f"Wynik mnożenia dwóch liczb: '{user_number1}' oraz '{user_number2}' = {user_number1 * user_number2}")
elif user_number1 < user_number2:
    print(f"Wynik odejmowania dwóch liczb: '{user_number2}' oraz '{user_number1}' = {user_number2 - user_number1}")
    if user_number1 != 0:
        print(f"Wynik dzielenia dwóch liczb: '{user_number2}' oraz '{user_number1}' = {user_number2 / user_number1}")
    else:
        print(f"Wynik dzielenia dwóch liczb: '{user_number2}' oraz '{user_number1}' nie może dojść do skutku, ponieważ nie można dzielić przez liczbę 0!!!")
elif user_number1 == user_number2:
    print(f"Obie wprowadzone liczby są takie same '{user_number1}'.")