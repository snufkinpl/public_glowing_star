student_ID_number = int(input("Podaj swój numer albumu: "))

if student_ID_number >= 1 and student_ID_number < 4000:
    print("Jesteś za długo studentem!")
elif student_ID_number >= 4000 and student_ID_number <= 10000:
    print("Twój czas studiowania dobiega końca.")
else:
    print("Niewłaściwy numer")
