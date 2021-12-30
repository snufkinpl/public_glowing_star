digits = {
    "1": "Jeden",
    "2": "Dwa",
    "3": "Trzy",
    "4": "Cztery",
    "5": "Pięć",
    "6": "Sześć",
    "7": "Siedem",
    "8": "Osiem",
    "9": "Dziewięć",
    "0": "Zero",
    " ": ""
              }
result = ""
phone = input("Wprowadź numer telefonu: ")
for character in phone:
    if character != " ":
        result += digits.get(character, "") + " "
    else:
        continue
print(result)


print("*" * 30)
print("KONIEC PROGRAMU.")