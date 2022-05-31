# print("Первое Задание")
# Entered_number = int(input("Введите время в секундах:" ));
# amount_of_days = (Entered_number // 86400)
# print(amount_of_days, "days")
# amount_of_hours = Entered_number % 86400 // 3600
# print(amount_of_hours, "hours")
# amount_of_minutes = Entered_number % 86400 % 3600 // 60
# print(amount_of_minutes, "minutes")
# amount_of_seconds = Entered_number % 86400 % 3600 % 60
# print(amount_of_seconds, "seconds")

# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# # c. * Решить задачу под пунктом b, не создавая новый список

print("Второе Задание")
my_list =[]
for num in range(1, 1000, 2):
    my_list.append(num ** 3)
    print(my_list)

