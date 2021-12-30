#Wytyczne projektu
#Użytkownik wprowadza nazwę celu oraz czas na jego osiągnięcie poprzez podanie daty w postaci:yyyy-mm-dd
#Na ekranie pojawia się informacja, ile czasu pozostało na osiągnięcie celu (w dniach)

import information_from_user
import time_and_execute


print(f"Użytkowniku, do osiągnięcia Twojego celu: {information_from_user.goal}, zostało Ci {time_and_execute.date_difference} dni.")

