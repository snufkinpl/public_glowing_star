# 5.	Napisać program, który posortuje metodą bąbelkową 7-elementową tablicę liczb całkowitych podanych przez użytkownika i wypisze na ekranie tablicę posortowaną.

def bubblesort(list_of_numbers):
    for n in range(len(list_of_numbers) - 1, 0, -1):
        for i in range(n):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]

list_of_numbers = []
for i in range(7):
    temp_number = int(input(f"Wprowadź liczbę{i+1}: "))
    list_of_numbers.append(temp_number)

print(f"Tak wygląda nieposortowana lista: {list_of_numbers}")
bubblesort(list_of_numbers)
print(f"Tak wygląda posortowana lista: {list_of_numbers}")


