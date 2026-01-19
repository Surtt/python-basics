# price = input("Введите цену: ")
#
# formatted_str = price.strip().lower()
# splitted_list = formatted_str.split(" ")
#
# if len(splitted_list) < 2:
#     print("Некорректный формат суммы")
# else:
#     if "руб" in splitted_list[1]:
#         rub = splitted_list[0]
#
#         if not rub.isdigit():
#             print("Некорректный формат суммы")
#         else:
#             if len(splitted_list) >= 4 and "коп" in splitted_list[3]:
#                 kop = splitted_list[2]
#
#                 if not kop.isdigit():
#                     print("Некорректный формат суммы")
#                 else:
#                     kop_formatted = kop.zfill(2)
#                     print(f"{rub}.{kop_formatted} ₽")
#             else:
#                 print(f"{rub}.00 ₽")

MENU_LIST = (
    "Добавить расход",
    "Показать все расходы",
    "Показать сумму и средний расход",
    "Удалить расход по номеру",
    "Выход",
)

while True:
    print()
    for index, item in enumerate(MENU_LIST, start=1):
        print(f"{index}. {item}")
    users_answer = int(input("Выберите пункт меню:\n"))
    if users_answer == 5:
        print("До свидания!")
        break
    else:
        print("В разработке...\n")
