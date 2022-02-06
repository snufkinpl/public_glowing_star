# 4.	Napisać program, który dla zadeklarowanej 10-elementowej tablicy liczb całkowitych z zakresu -15..15 wypisze sumę liczb parzystych i sumę liczb nieparzystych z tej tablicy.

list_of_numbers = []
for i in range(10):
    temp_number = int(input(f"Wprowadź liczbę{i+1} całkowitą z przedziału -15..15: "))
    list_of_numbers.append(temp_number)
    while True:
        if -15 <= list_of_numbers[i] <= 15:
            break
        else:
            list_of_numbers[i] = int(input(f"Wprowadź POPRAWNIE liczbę{i + 1} całkowitą z przedziału -15..15: "))

result_of_sum_positive = 0
result_of_sum_negative = 0

for i in range(10):
    if list_of_numbers[i] == 0:
        continue
    if list_of_numbers[i] % 2 == 0:
        result_of_sum_positive += list_of_numbers[i]
    else:
        result_of_sum_negative += list_of_numbers[i]

print(f"Oto suma liczb parzystych w tablicy: {result_of_sum_positive}")
print(f"Oto suma liczb nieparzystych w tablicy: {result_of_sum_negative}")
