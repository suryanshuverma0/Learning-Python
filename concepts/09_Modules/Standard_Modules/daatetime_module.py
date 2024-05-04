'''
The datetime module in Python is a powerful tool for working with dates and times. It provides classes for manipulating dates and times in both simple and complex ways.
'''
import datetime

# Creating a date object
today = datetime.date.today()
# print("Today's date:", today)

# Creating a custom date object
custom_date = datetime.date(2022, 5, 4)
# print("Custom date:", custom_date)

current_time = datetime.time(15, 30, 45)
# print("Current time:", current_time)

now = datetime.datetime.now()
# print("Current time:", now)

now_time = datetime.datetime.now().time()
# print("Current time:", now_time)

now_time_hour = datetime.datetime.now().time().hour
# print("Current hour:", now_time_hour)


now = datetime.datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)


date_string = "2022-05-04 15:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)


# Creating a timedelta object
delta = datetime.timedelta(days=5, hours=3)
print("Timedelta:", delta)
