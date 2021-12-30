# 5.	Program liczący sumę cyfr podanej przez użytkownika liczby.

user_number = input("Podaj liczbę, dla której zostanie policzona suma jej cyfr: ")

result_digits_sum = 0

for number in range(len(user_number)):
    result_digits_sum += int(user_number[number])

print(f"Liczba użytkownika = {user_number}")
print(f"Suma cyfr użytkownika = {result_digits_sum}")
