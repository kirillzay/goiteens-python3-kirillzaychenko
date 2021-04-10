# 1 задача
transformers = {"Оптімус Прайм": "Грузовик Peterbilt 379", "Бамблбі": "Chevrolet Camaro", "Джаз": "Porsche 935 Turbo" }
# 2 задача
for i in transformers:
    if i == "Оптімус Прайм":
        print("Оптімус прайм прибув")

# 3 задача
transformersWeight = { "Оптімус": 5000, "Бамблбі": 2500, "Джаз": 3000 }
alltransformersWeight = 0
for i in transformersWeight:
    alltransformersWeight = alltransformersWeight + transformersWeight[i]
print(alltransformersWeight)

# 4 задача
megatron = ("Megatron", "Кібертронський винищувач, Танк, Кібертронський Зорельот.", "Десептикон")
for i in megatron:
    if i == "Десептикон":
        print("Мегатрон ворог!!!")

# 5 задача
transformers["Сентінел Прайм"] = "Пожежна машина"
print(transformers)