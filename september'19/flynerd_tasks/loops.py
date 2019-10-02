name = input("Podaj swoje imię: ")
surname = input("Podaj swoje nazwisko: ")
phone_number = input("Podaj swój numer telefonu: ")

print(name.isalpha())
print(surname.isalpha())
print(phone_number.isdigit())


name = name.capitalize()
surname = surname.capitalize()
print(name, surname)
phone_number = phone_number.replace("-","").replace(" ","")
print(phone_number)
#phone_number = phone_number.replace(" ","")
#print(phone_number)

if name[-1] == "a":
    print("Jesteś kobietą :)")
else:
    print("Jesteś mężczyzną :>")

persona1 = name + surname + phone_number
print(name, surname, phone_number)
print("Ilość znaków persony:", len(persona1))
print("Ilość znaków persony bez numeru telefonu:", len(persona1)-9)
