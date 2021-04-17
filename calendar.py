print("Привіт це мій календар")
print("Виберіть функцію")
print("1. Записати нову подію")
print("2. Прочитати всі події")
print("3. Вийти")
selected_function = input("введіть функцію яку ви вибрали: ")

if selected_function == "1":
    neu_date = input("Введіть дату: ")
    calendar = open("calendar.txt", "a")
    calendar.write("\n" + neu_date)
    calendar.close()
if selected_function == "2":
    calendar = open("calendar.txt", "r")
    print(calendar.read())
if selected_function == "3":
    print("Допобачення!!!")

input("натисніть будь яку клавішу щоб вийти: ")