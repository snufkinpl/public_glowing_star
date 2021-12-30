import math


print("Podaj liczby w takiej postaci: liczba naturalna - n oraz liczba rzeczywista - x do policzenia P i W:\nP = 1*2*...*n\nW = x*x*...*x = x do potęgi n.")
user_natural_number = int(input("Podaj liczbę naturalną: "))
user_real_number = float(input("Podaj liczbę rzeczywistą: "))

result_for_n = 1
result_for_x = 1

if user_natural_number > 0:
    for number in range(1, user_natural_number+1):
        result_for_n *= number
elif user_natural_number == 0:
    result_for_n = 0
else:
    result_for_n = f"podana liczba: '{user_natural_number}' nie jest liczbą naturalną."

if user_natural_number >= 0:
    for number in range(user_natural_number):
        result_for_x *= user_real_number

print(f"\nWyniki operacji matematycznych:\nP = {result_for_n}\nW = {result_for_x}")
if user_natural_number > 0:
    print(f"Można też użyć biblioteki/modułu math do obliczeń matematycznych i użyć funkcji math.factorial, aby uzyskać żądaną operację P = {math.factorial(user_natural_number)} (tylko dla n > 0)")
print(f"Można też użyć biblioteki/modułu math do obliczeń matematycznych i użyć funkcji math.pow, aby uzyskać żądaną operację W = {math.pow(user_real_number,user_natural_number)}")

