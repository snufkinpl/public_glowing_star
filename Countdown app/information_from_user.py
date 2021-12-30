import datetime


user_input = input("Wprowadź nazwę celu oraz jego końcową datę w postaci yyyy-mm-dd. Nazwę celu oraz datę oddziel dwukropkiem.\n")
list_of_user_input = user_input.split(":")
goal = list_of_user_input[0]
deadline = list_of_user_input[1]
user_date = datetime.date(int(deadline[0:4]), int(deadline[5:7]), int(deadline[8:10]))
