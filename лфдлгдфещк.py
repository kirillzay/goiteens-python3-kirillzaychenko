number1 = int(input("1 число: "))
diya = input("дія: ")
number2 = int(input("2 число: "))
if diya == "+":
    sum0 = number1 + number2
    print("результат: ",sum0)
elif diya == "-":
    sum0 = number1 - number2
    print("результат: ", sum0)
elif diya == "/":
    sum0 = number1 / number2
    print("результат: ", sum0)
elif diya == "*":
    sum0 = number1 * number2
    print("результат: ", sum0)
elif diya == "Kirill":
    print("це секретна операція Кирило Зайченко це розробник ціеЇ програми")
else:
    print("некоректна операція")

input("натисніть будь-яку клавішу, щоб закрити калькулятор: ")