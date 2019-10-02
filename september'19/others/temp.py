import random
wordSet = ["amazing", "surprise", "advanced", "building", "mysterious"]
random_word = random.choice(wordSet)
x_word=list(random_word)
random.shuffle(x_word)
print("Guess this word: ")
print("".join(x_word))

while True:
    n = input()
    n.lower()
    if n == random_word:
        print("You won!")
        break
    elif n == "q":
        print("End!")
        break
    else:
        print("Try again.")
