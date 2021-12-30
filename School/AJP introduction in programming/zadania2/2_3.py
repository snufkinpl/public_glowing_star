# 3.	Poprosić użytkownika o podanie liczby. Program powinien liczyć sumę liczb parzystych z przedziału od 0 do podanej liczby.

user_number = int(input("Podaj liczbę, dla której zostanie policzona suma liczb: "))

result_sum = 0

if user_number > 0:
    for number in range(user_number+1):
        if number % 2 == 0:
            result_sum += number
    print(f"Suma liczb parzystych = {result_sum}")
elif user_number == 0:
    print(f"Suma liczb = {result_sum}")
else:
    print(f"Podałeś liczbę ujemną.")
