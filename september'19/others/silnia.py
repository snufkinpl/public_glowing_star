user_choice = int(input("Podaj dowolną liczbę naturalną do 100: "))
silnia = 1
if user_choice != 0:
  while True:
    if silnia == user_choice:
      print(f"{user_choice}! jest równa {silnia}")
      break
    else:
      for number in range(2, user_choice + 1):
        silnia *= number
      print(f"{user_choice}! jest równa {silnia}")
      break

else:
  print("0! jest równa 1")

print("*" * 30)
print("KONIEC PROGRAMU.")

