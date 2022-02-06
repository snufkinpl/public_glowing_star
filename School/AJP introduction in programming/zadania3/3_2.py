# 2.	Napisać program, który wczytuje tablicę 10 liczb rzeczywistych z zakresu -70 + 70 i wypisuje jej elementy na ekranie monitora. Następnie program oblicza sumę tych elementów tablicy, które należą do przedziału [-5,10] oraz wypisuje ją na ekranie.

list_of_numbers = []
for i in range(10):
    temp_number = float(input(f"Wprowadź liczbę{i+1} rzeczywistą z przedziału -70..70: "))
    list_of_numbers.append(temp_number)
    while True:
        if -70 <= list_of_numbers[i] <= 70:
            break
        else:
            list_of_numbers[i] = float(input(f"Wprowadź liczbę{i + 1} rzeczywistą z przedziału -70..70: "))

print(f"Oto wprowadzone liczby do tablicy: {list_of_numbers}")

result_of_sum = 0
for i in range(10):
    if -5 <= list_of_numbers[i] <= 10:
        result_of_sum += list_of_numbers[i]

print(f"Oto suma liczb w tablicy, które mieszczą się w przedziale [-5, 10]: {result_of_sum}")






