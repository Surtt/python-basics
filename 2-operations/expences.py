food = input("Введите траты на еду за месяц: ")
transport = input("Введите траты на транспорт за месяц: ")
entertainment = input("Введите траты на развлечения за месяц: ")

print(
    "Траты за месяц составляют:", float(food) + float(transport) + float(entertainment)
)
print(
    "Средние траты за месяц составляют:",
    (float(food) + float(transport) + float(entertainment)) / 3,
)
