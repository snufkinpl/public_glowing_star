print("Podaj liczby w takiej postaci (liczba1, liczba2) do policzenia ich sumy.")
user_number1 = int(input("Podaj liczbę 1: "))
user_number2 = int(input("Podaj liczbę 2: "))

result = 0

if user_number1 <= user_number2:
    for number in range(user_number1, user_number2+1):
        result += number
    print(f"Suma wszystkich liczb z podanego przedziału od {user_number1} do {user_number2} wynosi = {result}.")
else:
    print("Podany przedział jest nieprawidłowy.")
