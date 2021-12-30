def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


user_number = int(input("Podaj liczbę: "))
print(fizz_buzz(user_number))
print("*" * 30)
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print(fizz_buzz(86))
print("*" * 30)
print("KONIEC PROGRAMU.")