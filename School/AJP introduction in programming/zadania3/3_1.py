# 1.	Napisać program, który wczytuje tablicę 10 liczb rzeczywistych z zakresu 0..10 i wypisuje jej elementy na ekranie monitora. Następnie program szuka elementu najmniejszego tablicy oraz miejsca (indeksu), na którym ten element się znajduje oraz wypisuje je na ekranie.

list_of_numbers = []
for i in range(10):
    temp_number = float(input(f"Wprowadź liczbę{i+1} rzeczywistą z przedziału 0..10: "))
    list_of_numbers.append(temp_number)
    while True:
        if 0 <= list_of_numbers[i] <= 10:
            break
        else:
            list_of_numbers[i] = float(input(f"Wprowadź liczbę{i + 1} rzeczywistą z przedziału 0..10: "))

print(f"Oto wprowadzone liczby do tablicy: {list_of_numbers}")
print(f"Najmniejsza liczba wynosi: {min(list_of_numbers)}")
print(f"Index w tablicy wynosi: {list_of_numbers.index(min(list_of_numbers))}")





