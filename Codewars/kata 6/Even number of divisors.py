def oddity(n):
    result = []
    for number in range(1, n+1):
        if n % number == 0:
            result.append(number)
    print(result)
    if len(result) % 2 == 0:
        return "even"
    else:
        return "odd"


user_number = int(input("Podaj liczbę, aby sprawdzić czy ilość jej dzielników jest parzysta czy nieparzysta: "))
print(oddity(user_number))
