import sys

books = {"Война и мир": "Лев Толстой", "Мастер и Маргарита": "Михаил Булгаков"}
books["Преступление и наказание"] = "Федор Достоевский"
books["Анна Каренина"] = "Лев Толстой"
books["Идиот"] = "Федор Достоевский"
books["Отцы и дети"] = "Иван Тургенев"


def sort_books(books_dict, sort_by):
    if sort_by == "author":
        sorted_books = sorted(books_dict.items(), key=lambda item: item[1])
    else:
        sorted_books = sorted(books_dict.items(), key=lambda item: item[0])

    return list(map(lambda item: f"{item[0]} — {item[1]}", sorted_books))


def filter_books(books_dict, author_filter):
    filtered = filter(lambda item: author_filter in item[1], books_dict.items())
    return list(map(lambda item: f"{item[0]} — {item[1]}", filtered))


match sys.argv[1]:
    case "sort":
        result = sort_books(books, sys.argv[2])
        for line in result:
            print(line)
    case "filter":
        result = filter_books(books, sys.argv[2])
        for line in result:
            print(line)
    case _:
        print("Неизвестная команда. Используйте: sort или filter")
