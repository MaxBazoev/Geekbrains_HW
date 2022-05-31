Entered_number = int(input("Введите время в секундах:" ));
amount_of_days = (Entered_number // 86400)
print(amount_of_days, "days")
amount_of_hours = Entered_number % 86400 // 3600
print(amount_of_hours, "hours")
amount_of_minutes = Entered_number % 86400 % 3600 // 60
print(amount_of_minutes, "minutes")
amount_of_seconds = Entered_number % 86400 % 3600 % 60
print(amount_of_seconds, "seconds")

