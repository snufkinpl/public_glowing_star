egipts = [[3, 4, 5], [6, 8, 10], [9, 12, 15], [15, 20, 25]]
bok_A = int(input("Podaj pierwszy bok: "))
bok_B = int(input("Podaj drugi bok: "))
bok_C = int(input("Podaj trzeci bok: "))
print("*" * 33)

list = [bok_A, bok_B, bok_C]
list.sort()
print("Wydrukowana lista z długościami boków potencjalnego trójkąta:", list)

kwadrat_A = list[0] ** 2
kwadrat_B = list[1] ** 2
kwadrat_C = list[2] ** 2

if list[2] > list[0] and list[2] > list[1]:
    print(kwadrat_A, "+", kwadrat_B, "=", kwadrat_C)
    if kwadrat_A + kwadrat_B == kwadrat_C:
        print("To jest trójkąt pitagorejski")
        if [list[0], list[1], list[2]] in egipts:
            print("To jest również trójkąt egipski!")
    else:
        print("Nie jest to trójkąt pitagorejski")
else:
    print("Nie można utworzyć trójkąta prostokątnego :c")

print("*" * 33)
print("KONIEC PROGRAMU.")

