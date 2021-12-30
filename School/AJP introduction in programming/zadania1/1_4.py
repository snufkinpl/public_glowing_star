import math


def main():
    quit_program = 0
    while quit_program != "N":
        user_math_operation_choice = input("Podaj operację matematyczną, którą chcesz wykonać:\n1 - aby wykonać mnożenie zmiennych,\n2 - aby wykonać dzielenia zmiennych,\n3 - aby wykonać dodawanie zmiennych,\n4 - aby wykonać odejmowanie zmiennych,\n5 - aby wykoanć pierwiastek z sumy.\nWybór: ")
        user_number1 = int(input("Podaj liczbę 1: "))
        user_number2 = int(input("Podaj liczbę 2: "))
        if user_math_operation_choice == "1":
            result = user_number1 * user_number2
        elif user_math_operation_choice == "2":
            result = user_number1 / user_number2
        elif user_math_operation_choice == "3":
            result = user_number1 + user_number2
        elif user_math_operation_choice == "4":
            result = user_number1 - user_number2
        elif user_math_operation_choice == "5":
            result = math.sqrt(user_number1 + user_number2)
        else:
            print(f"Nie ma takiej operacji matematycznej jak '{user_math_operation_choice}'. Spróbuj ponownie.")
            continue

        print(f"Wybór działania '{user_math_operation_choice}' Twoich liczb: {user_number1} i {user_number2} = {result}.")
        while True:
            quit_program = input("Czy chcesz kontynuować? Wpisz literę t lub n: ").capitalize()
            if quit_program == "T" or quit_program == "N":
                break


main()
