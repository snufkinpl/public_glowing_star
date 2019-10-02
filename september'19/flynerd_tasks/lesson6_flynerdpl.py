age = int(input("Ile masz lat?: "))
if age < 18:
    print("Użytkownik niepełnoletni. Pozostało Ci", 18-age, "lat do pełnoletności.")
else:
    print("Użytkownik pełnoletni.")
if age >= 100:
    print("Użytkowniku, życzymy Ci 200lat! ♫♫♫")
