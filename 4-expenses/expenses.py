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

exps = []


def add_expense(expenses: list[float], value: float) -> None:
    expenses.append(value)
    print("Расход добавлен.")


def delete_expense(expenses: list[float], index: int) -> None:
    expenses.pop(index)
    print("Расход удален.")


def get_total(expenses: list[float]) -> float:
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    return get_total(expenses) / len(expenses)


def print_report(expenses: list[float]) -> None:
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense} ₽")


while True:
    print()
    for index, item in enumerate(MENU_LIST, start=1):
        print(f"{index}. {item}")
    users_answer = int(input("Выберите пункт меню:\n"))
    match users_answer:
        case 1:
            add_expense(exps, float(input("Введите сумму расхода: ")))
            print(exps)
        case 2:
            print(print_report(exps))
        case 3:
            get_total_value = get_total(exps)
            get_average_value = get_average(exps)
            print(f"Сумма всех расходов: {get_total_value}")
            print(f"Средний расход: {get_average_value}")
        case 4:
            delete_expense(exps, int(input("Введите номер расхода для удаления: ")) - 1)
            print(exps)
        case 5:
            print("До свидания!")
            break
