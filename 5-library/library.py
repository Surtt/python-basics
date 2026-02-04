import sys


class LibraryError(Exception):
    pass


class UnknownCommandError(LibraryError):
    pass


class InvalidSortKeyError(LibraryError):
    pass


class EmptyFilterKeyError(LibraryError):
    pass


books = {"Война и мир": "Лев Толстой", "Мастер и Маргарита": "Михаил Булгаков"}
books["Преступление и наказание"] = "Федор Достоевский"
books["Анна Каренина"] = "Лев Толстой"
books["Идиот"] = "Федор Достоевский"
books["Отцы и дети"] = "Иван Тургенев"


def sort_books(books_dict, sort_by):
    if sort_by == "author":
        sorted_books = sorted(books_dict.items(), key=lambda item: item[1])
    elif sort_by == "title":
        sorted_books = sorted(books_dict.items(), key=lambda item: item[0])
    else:
        raise InvalidSortKeyError(f"Неверный ключ сортировки: {sort_by}")

    return list(map(lambda item: f"{item[0]} — {item[1]}", sorted_books))


def filter_books(books_dict, author_filter):
    if not author_filter:
        raise EmptyFilterKeyError("Ключ фильтрации не может быть пустым")
    filtered = filter(lambda item: author_filter in item[1], books_dict.items())
    return list(map(lambda item: f"{item[0]} — {item[1]}", filtered))


match sys.argv[1]:
    case "sort":
        try:
            result = sort_books(books, sys.argv[2])
            for line in result:
                print(line)
        except InvalidSortKeyError as e:
            print(e)
    case "filter":
        try:
            result = filter_books(books, sys.argv[2])
            for line in result:
                print(line)
        except EmptyFilterKeyError as e:
            print(e)
    case _:
        try:
            raise UnknownCommandError(f"Неизвестная команда: {sys.argv[1]}")
        except UnknownCommandError as e:
            print(e)
