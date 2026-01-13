price = input("Введите цену: ")

formatted_str = price.strip().lower()
splitted_list = formatted_str.split(" ")

if len(splitted_list) < 2:
    print("Некорректный формат суммы")
else:
    if "руб" in splitted_list[1]:
        rub = splitted_list[0]

        if not rub.isdigit():
            print("Некорректный формат суммы")
        else:
            if len(splitted_list) >= 4 and "коп" in splitted_list[3]:
                kop = splitted_list[2]

                if not kop.isdigit():
                    print("Некорректный формат суммы")
                else:
                    kop_formatted = kop.zfill(2)
                    print(f"{rub}.{kop_formatted} ₽")
            else:
                print(f"{rub}.00 ₽")
