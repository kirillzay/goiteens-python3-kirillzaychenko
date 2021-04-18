# #1 задача
def print_my_name(my_name):
    print(my_name)


print_my_name("kirill")

#2 задача 3 задача

def calculator(num1, num2, action):
    if action == "+":
        result = num1 + num2
        print(result)
    elif action == "-":
        result = num1 - num2
        print(result)
    elif action == "/":
        result = num1 / num2
        print(result)
    elif action == "*":
        result = num1 * num2
        print(result)

action = input("Input action ")


calculator(5, 2, action)

#4 задача
def even_number(num):
    if num % 2==0:
        print("акція діє")
    else:
        print("Акція не діє")


even_number( int(input("input number: ")))


# 5 задача
def print_list(l):
    print(l)

names = ["Ярослав", "Богдан", "Катя"]
print_list(names)

#6 задача
names.append ("Євген")
print(names)

#7 задача
def is_evgen(names):
    if "Євген" in names: 
        print("у списку є ім'я Євген")
    else:
        print("у списку немає ім'я Євген")

is_evgen(names)

    