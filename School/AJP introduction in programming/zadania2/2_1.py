# 1.	Poprosić użytkownika o podanie liczby. Program wykorzystując pętlę For liczy sumę od 0 do liczby podanej przez użytkownika  i  średnią liczb.

user_number = int(input("Podaj liczbę, dla której zostanie policzona suma oraz średnia liczb: "))

result_sum = 0

if user_number > 0:
    for number in range(user_number+1):
        result_sum += number
    result_mean = result_sum / user_number
    print(f"Suma liczb = {result_sum}")
    print(f"Średnia liczb = {result_mean}")
elif user_number == 0:
    print(f"Suma liczb = {result_sum}\nŚrednia liczb również wynosi 0")
else:
    print(f"Podałeś liczbę ujemną.")
