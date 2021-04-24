#functions
def menu():
    print("Привіт це мій календар")
    print("Виберіть функцію")
    print("1. Записати нову подію")
    print("2. Прочитати всі події")
    print("3. Вийти")

    return input("введіть функцію яку ви вибрали: ")


def addevent():
    neu_date = input("Введіть подію в форматі Пріоритет/Дата (yyyy.mm.dd)/Назва: ")
    calendar = open("calendar.txt", "a")
    calendar.write("\n" + neu_date)
    calendar.close()

def sortedbypriority(all_events):
    return sorted(all_events, key= lambda f : f[0])

def sortedbydate(all_events):
   return sorted(all_events, key= lambda f : f[1])
#main program


selected_function = menu()
all_events = list()
if selected_function == "1":
    addevent()
if selected_function == "2":
    #calendar = neu_date.sorted(open("calendar.txt", "r"))
    #print(calendar.read())
    calendar = open("calendar.txt", "r")
    lst=calendar.readlines()
    print(lst)
    for ln in lst:
        all_events.append(ln.split("/"))
    print(all_events)
    sorted_by_priority = sortedbypriority(all_events)
    print("Сортування за пріоритетом: ", sorted_by_priority)
    sorted_by_date = sortedbydate(all_events)
    print("сортування за датою: ", sorted_by_date)

    
if selected_function == "3":
    print("Допобачення!!!")

input("натисніть будь яку клавішу щоб вийти: ")
