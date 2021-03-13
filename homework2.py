#перша задача
years = int(input("кількість років: "))
terms = years / 4
if terms > 2:
    print("Президент не може бути на посту президента більше 2 термінів")
else:
    print("президент був на пості президента ",terms," термінів")
#друга задача
president = input("введіть ім'я президента:")
George_Washington = 2
Thomas_Jefferson = 2
Herbert_Hoover = 1
Barack_Obama = 2
if  president== "George Washington":
    print(George_Washington * 4, " років на посаді був Джордж Вашингтон")
elif president== "Thomas Jefferson":
    print(Thomas_Jefferson * 4, " років на посаді був Томас Джеферсон")
elif president== "Herbert Hoover":
    print(Herbert_Hoover * 4, " років на посаді був Херберт Хувер")
elif president== "Barack Obama":
    print(Barack_Obama * 4, "років на посаді був Барак Обама")
else:
    print("у нас немає данних про такого президента")
#третя задача
game_ = input("введіть тип гри: ")
if game_== "2D":
    print("Teraria")
elif game_== "3D":
    print("Minecraft")
else:
    print("у нас нема таких ігор")
#четверта задача
Fortnite = 2017
CS_GO = 2012
if CS_GO < Fortnite:
    print("CS GO на " ,Fortnite - CS_GO, " років старша за Fortnite")
else:
    print("CS GO на " ,CS_GO - Fortnite, " років молодша за Fortnite")
#п'ята задача
all_gamer_HP = 100
damage_skelet = 15
damage_zombe = 5
damage_spider = 40
all_damage_skelet = damage_skelet * 1
all_damage_zombe = damage_zombe * 5
all_damage_spider = damage_spider * 2
all_damage = all_damage_skelet + all_damage_zombe + all_damage_spider
if all_gamer_HP < all_damage:
    print("you die!")
else:
    print("You have only " ,all_gamer_HP - all_damage)
    
input("натисніть будь-яку клавішу щоб закрити файл")