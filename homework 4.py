#1 задача
simpson_famili = ["Гомер", "Мардж", "Ліза", "Барт", "Мегі"]
print (simpson_famili)
#2 задача
simpson_famili.append("Дідусь")
print (simpson_famili)
#3 задача
simpson_famili.remove("Дідусь")
simpson_famili.append("Абрахам")
print (simpson_famili)
#4 задача
gomer_money =  [100, 50, 50, 100, 200]
gomer_money = (sum(gomer_money))
print(gomer_money)
#5 задача
donuts = ["Ягідні", "Вишневі", "Шоколадні", "Карамельні"]
for donut in donuts:
    if donut == "Вишневі":
        print ("У списку є вишневі пончики")
#6 задача
buttons = ["Alt", "Shift", "Ctrl"]
Alt = 0
Shift = 0
Ctrl = 0
print (buttons)
qwest = input("яку клавішу натиснути ?: ")
if qwest == ("Alt"):
    print("Гомера звільнять")
elif qwest == ("Shift"):
    print("Гомера звільнять")
elif qwest == ("Ctrl"):
    print("ТРЕВООООООООВАААААА!!!")
#7 задача
print (100 * "Я не буду їсти палички Бобо на уроці")
#8 задача
marg_know = ["Математика", "Англійська мова", "Фізика"]
marg__know = len(marg_know)
if marg__know < 5:
    print ("Мардж не може отримати грант")
else:
    print ("Мардж отримала грант")
#9 задача
for i in range(1,50):
    print(i/100)