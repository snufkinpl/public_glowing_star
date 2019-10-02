list = []
name = input("Podaj swoje imię: ")
if name[-1].lower() == "a":
    print("Witamy Panią!")
else:
    print("Witamy Pana!")

if name in list:
    print("Mamy Twoje imię na liście zaproszenia. Proszę wejść do lokalu!")
else:
    print("Nie możesz dzisiaj wejść. Dodamy Cię na listę następnej imprezy.")
    list.append(name)

print("A oto lista gości:", list)


#Program fajny do rozbudowy :)