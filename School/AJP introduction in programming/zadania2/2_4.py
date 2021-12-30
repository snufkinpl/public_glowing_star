# 4.	Napisać program, który zlicza ilość podanych przez użytkownika liczb, ale tylko podzielnych przez 3, do kiedy ilość tych liczb nie przekroczy 20.

user_number = int(input("Podaj liczbę, dla której zostanie policzona ilość liczb podzielnych przez 3: "))

numbers_divided_by3 = []

if user_number >= 0:
    for number in range(0, user_number+1):
        if number % 3 == 0:
            if len(numbers_divided_by3) < 20:
                numbers_divided_by3.append(number)
            else:
                break
    print(f"Ilość liczb podzielnych przez 3 = {len(numbers_divided_by3)}")
else:
    print(f"Podałeś liczbę ujemną.")