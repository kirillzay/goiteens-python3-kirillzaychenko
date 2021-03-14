#задача 1
speed_hour = 200
distance = 600
time = distance / speed_hour
print("за" ,time ,"години марседес проїхав 600 км")
#задача 2
if time > 60:
    print("мерседес їхав більше години")
else:
    print("мерседес їхав менше години")
#задача 3
cars = ["audi","BMW","Porche"]
print(cars[0])
#задача 4
print(len(cars))
#задача 5
cars.append("Tesla")
print(cars)
#задача 6
cars_Aleksya = ["Audi R8 e tron","Mercedes Benz gle 400","Tesla Model S"]
cars_Oleg = ["Лада Калина","Запорожець"]
kilk_Aleksya = len(cars_Aleksya)
kilk_Oleg = len(cars_Oleg)
if kilk_Aleksya > kilk_Oleg:
    print("у Алексі більше машин")
else:
    print("у Олега більше машин")