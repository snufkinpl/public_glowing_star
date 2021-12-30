numbers_divided_by3 = []
numbers_divided_by4 = []

for number in range(0, 101):
    if number % 3 == 0:
        numbers_divided_by3.append(number)

for number in range(0, 101):
    if number % 4 == 0:
        numbers_divided_by4.append(number)

print(numbers_divided_by3)
print(numbers_divided_by4)
