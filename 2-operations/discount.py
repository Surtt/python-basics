price = input("Введите стоимость товара: ")
discount = input("Введите размер скидки: ")
print(
    "Цена со скидкой составляет:", float(price) - (float(price) * float(discount) / 100)
)
