import random


class Dice:
    def roll():
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        return number1, number2
    def info():
        return "I am k6 dice."


print(Dice.roll())
print(Dice.info())
