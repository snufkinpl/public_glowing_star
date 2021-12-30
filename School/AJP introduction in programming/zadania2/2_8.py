# 8.	Program wyznaczający największy wspólny dzielnik dwóch liczb wprowadzanych przez użytkownika.

user_number1 = int(input("Podaj liczbę 1, dla której zostanie wyznaczony NWD dwóch liczb: "))
user_number2 = int(input("Podaj liczbę 2, dla której zostanie wyznaczony NWD dwóch liczb: "))
temp_number1 = user_number1
temp_number2 = user_number2

if temp_number1 < temp_number2:
    temp_number = temp_number1
    temp_number1 = temp_number2
    temp_number2 = temp_number

result = temp_number1 % temp_number2
# print(f"Show actual result = {result}")
while True:
    if result == 0:
        print(f"NWD dwóch liczb: [{user_number1}] oraz [{user_number2}] wynosi {temp_number2}")
        break
    else:
        temp_number1 = temp_number2
        temp_number2 = result
        result = temp_number1 % temp_number2
