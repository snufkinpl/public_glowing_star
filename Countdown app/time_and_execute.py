import information_from_user
import datetime


date_difference = information_from_user.user_date - datetime.date.today()
date_difference = date_difference.days
