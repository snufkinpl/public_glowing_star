#Wytyczne projektu
#Użytkownik wprowadza nazwę celu oraz czas na jego osiągnięcie poprzez podanie daty w postaci:yyyy-mm-dd
#Na ekranie pojawia się informacja, ile czasu pozostało na osiągnięcie celu (w dniach)
import datetime


def information_from_user():
    user_input = input("Wprowadź nazwę celu oraz jego końcową datę w postaci yyyy-mm-dd. Nazwę celu oraz datę oddziel dwukropkiem.\n")
    list_of_user_input = user_input.split(":")
    goal = list_of_user_input[0]
    deadline = list_of_user_input[1]
    user_date = datetime.date(int(deadline[0:4]), int(deadline[5:7]), int(deadline[8:10]))
    return user_date, goal


def time_manipulation_and_execute(user_data):
    user_date = user_data[0]
    goal = user_data[1]
    date_difference = user_date - datetime.date.today()
    date_difference = date_difference.days
    print(f"Użytkowniku, do osiągnięcia Twojego celu: {goal}, zostało Ci {date_difference} dni.")


def main():
    #information_from_user()
    time_manipulation_and_execute(user_data=information_from_user())


main()

