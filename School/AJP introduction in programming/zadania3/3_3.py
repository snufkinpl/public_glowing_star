# 3.	Napisać program, który wczytuje tablicę 10 liczb całkowitych z zakresu -10..10 i wypisuje jej elementy na ekranie monitora. Następnie program oblicza sumę kwadratów tych elementów tablicy, które przy dzieleniu przez 4 dają resztę 2 lub są niedodatnie oraz wypisuje tę sumę na ekranie.

list_of_numbers = []
for i in range(10):
    temp_number = int(input(f"Wprowadź liczbę{i+1} całkowitą z przedziału -10..10: "))
    list_of_numbers.append(temp_number)
    while True:
        if -10 <= list_of_numbers[i] <= 10:
            break
        else:
            list_of_numbers[i] = int(input(f"Wprowadź liczbę{i + 1} całkowitą z przedziału -10..10: "))

result_of_sum = 0

for i in range(10):
    if list_of_numbers[i] % 4 == 2:
        result_of_sum += list_of_numbers[i] * list_of_numbers[i]
    if list_of_numbers[i] < 0:
        result_of_sum += list_of_numbers[i] * list_of_numbers[i]

print(f"Oto suma kwadratów liczb w tablicy, które spełniają warunek zadania: {result_of_sum}")