import random

word_DB = ["kruk", "wrona", "bank", "kino", "mózg", "kubek", "żmijka", "mydło", "miłość"]
word_random = random.choice(word_DB)

letters = list(word_random)
#print(letters)
random.shuffle(letters)
#print(letters)
check = "".join(letters) #przy krótkich słowach może być, że wymieszane litery dają taki sam układ co pierwotne słowo do zgadnięcia.
if check == word_random: #Robię to if'em choć lepiej by było to zrobić whilem dla większego bezpieczeństwa.
  #print(check)
  random.shuffle(letters)
  #print(letters)
#else:
  #print("Wszystko jest ok:)")

while True:
  print('Zgadnij słowo z liter:', " ".join(letters))
  print("Jeśli chcesz zakończyć zgadywanie wciśnij 'q' lub 'Q'.")
  print("*" * 25)
  user_word = input("Podaj poprawne słowo: ")
  if user_word.lower() == "q":
    print("Zakończyłeś program. Pa pa!")
    break
  if user_word == word_random:
    print(f"Brawo! Zgadłeś poprawnie słowo {word_random}.")
    break
  else:
    print("Spróbuj jeszcze raz :)")
    print("*" * 25)

print("*" * 30)
print("KONIEC PROGRAMU.")

