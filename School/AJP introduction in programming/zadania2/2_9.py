# 9.	Sprawdzenie czy tekst wprowadzany przez użytkownika jest palindromem.

def is_palindrom(user_string):
    palindrom = []
    temp_palindrom = []
    for letter in user_string:
        palindrom.append(letter)
    for i in range(len(palindrom)):
        # print(i) - numer kroku
        # print(palindrom[i]) pierwsza litera -> ostatnia
        # print(palindrom[-(i+1)]) ostatnia litera _> pierwsza
        if palindrom[i] == palindrom[-(i+1)]:
            temp_palindrom.append(palindrom[i])
        else:
            return f"'{user_string}' to nie jest palindrom."
    return f"Twój napis '{user_string}' jest palindromem."


    # print(f"Długość palindromu {len(palindrom)}.")



user_string = input("Podaj napis w celu sprawdzenia czy jest palindromem: ")
print(is_palindrom(user_string))