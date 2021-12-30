# 2.	Program wyświetlający osobno liczby parzyste i nieparzyste z przedziału od 0 do 100.

odd_numbers = []
even_numbers = []

for number in range(0, 101, 2):
    even_numbers.append(number)

for number in range(1, 101, 2):
    odd_numbers.append(number)

print(even_numbers)
print(odd_numbers)