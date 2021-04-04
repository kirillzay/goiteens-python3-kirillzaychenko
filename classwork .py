#1 задача
nums = {1: "one", 2: "two", 3: "three" }
print(nums[2])
#2 задача
for i in nums:
    print(i)

#3 задача
total = 0
for i in nums:
    total = total + i 
print(total)
#4 задача
for i, value in nums.items():
    print(i, " - ", value)

#5 задача
pharaons=("Клеопатра", "Рамзес", "Тутанхамон")
pharaons = list(pharaons)
for i in pharaons:
    names_b = len(i)
    if names_b > 8:
        print (i)

#6 задача
sarkofag_ = ("Сапфір", "Рубін", "Агат", "Бурштин")
n_stones = 0
for i in sarkofag_:
    n_stones = n_stones + 1
    if i == "Бурштин":
        print ("у саркофазі є бурштин")
print("загальна кількість каменів =" ,n_stones)

