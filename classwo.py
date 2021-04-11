# 1 задача 
presents = {"скейтборд", "футболку", "рюкзак", "цукерки (5 кг)", "мандарини"}
for i in presents:
    if i == "скейтборд":
        print("так скейтборд є")

# 2 задача 
money = {100, 200, 150, 300}
sum_ = sum(money)
mod_money = 200
all_money = sum_ + mod_money
print (all_money)

# 3 задача
gomer = {"Піцу", "Премію на роботі", "Касети з всіма випусками Клоуна Красті", "Шоколад"}
ned = {"Інструменти для лівшів", "Зелений чай", "Шоколад"}
for i in gomer:
    if i in ned:
        print (i)
# 4 задача
svichky = "happy birsday"
for i in svichky:
    print (i)

# 5 задача
names = ["Род", "Тод", "Мод", "Нед"]
for i in names:
    if "М" in i:
        print (i)

# 6 задача
zgadav = "я згадав що нед мені не віддав газонокосилку"
if "газон" in zgadav:
    print("гомер подумав про газон")

# 7 задача. В завданні є помилка: субота це Saturday, а не Sunday. Перевіряємо на Saturday.
import datetime

x = datetime.datetime.now()

print("tooday is", x.strftime("%A"))
if x.strftime("%A") == "Saturday":
    print("привіт субота")
else:
    print("НІІІІІ, хочу суботу")

# 8 задача
import datetime

x = datetime.datetime.now()

print(x.strftime("%m/%d/%y"))

# 9 задача
import datetime

x = datetime.datetime.now()

print(x.strftime("%X"))
