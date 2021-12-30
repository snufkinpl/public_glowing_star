# 6.	Program zamieniający liczbę podaną przez użytkownika na binarną.

user_number = int(input("Podaj liczbę, dla której zostanie podana wartość binarna: "))

user_number_calculate = user_number
user_number_binary = []
user_number_binary_reverse = []

while user_number_calculate != 0:
    user_number_binary.append(user_number_calculate % 2)
    user_number_calculate = int(user_number_calculate / 2)
    # print(f"Liczba użytkownika = {user_number_calculate}")
    # print(f"Liczba użytkownika w systemie binarnym = {user_number_binary}")


for element in range(1, len(user_number_binary)+1):
    # print(f"Wyświetl znak nr {element}, co odpowiada: {user_number_binary[-(element)]}")
    user_number_binary_reverse.append(user_number_binary[-(element)])
print(f"Podana liczba użytkownika '{user_number}' ma taką wartość w systemie binarnym = {user_number_binary_reverse}")



