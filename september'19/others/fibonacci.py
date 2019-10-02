def fibonacci(user_choice):
    if user_choice == 0:
        return 0
    if user_choice == 1:
        return 1
    f1 = 0
    f2 = 1
    for number in range(2, user_choice + 1):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    return temp


user_choice = int(input("Podaj liczbę z ciągu Fibonacciego: "))

result = fibonacci(user_choice)
print(f"F({user_choice}) = {result}")

print("*" * 30)
print("KONIEC PROGRAMU.")