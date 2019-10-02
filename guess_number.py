import random

number = random.randint(1, 30)
count = 1

while True:
    print("*" * 41)
    guess = int(input("Zgadnij liczbę w przedziale od 1 do 30: "))
    if number == guess:
        print("Brawo! To ta liczba!")
        print(f"Zgadłeś w {count} krokach.")
        break
    else:
        print("Próbuj dalej.")
        if guess > number:
            print("Twoja liczba jest MNIEJSZA.")
        else:
            print("Twoja liczba jest WIĘKSZA.")
    count += 1

print("*" * 30)
print("KONIEC PROGRAMU.")
