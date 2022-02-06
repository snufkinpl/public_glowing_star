# 1.	Napisać program, który wczytuje tablicę 10 liczb rzeczywistych z zakresu 0..10 i wypisuje jej elementy na ekranie monitora. Następnie program szuka elementu najmniejszego tablicy oraz miejsca (indeksu), na którym ten element się znajduje oraz wypisuje je na ekranie.

# METODA 2
user_input = input("Wprowadź 10 liczb z zakresu 0..10. Liczby oddziel przecinkiem. Przykład: 1,5,7,9,3,2,2,4,5,0\n")
list_of_user_input = user_input.split(",")

for i in range(len(list_of_user_input)):
    list_of_user_input[i] = int(list_of_user_input[i])

print(f"Oto wprowadzone liczby do tablicy: {list_of_user_input}")
print(f"Najmniejsza liczba wynosi: {min(list_of_user_input)}")
print(f"Index w tablicy wynosi: {list_of_user_input.index(min(list_of_user_input))}")