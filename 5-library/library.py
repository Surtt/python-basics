books = {"Война и мир": "Лев Толстой", "Мастер и Маргарита": "Михаил Булгаков"}
books["Преступление и наказание"] = "Федор Достоевский"
books["Анна Каренина"] = "Лев Толстой"
books["Идиот"] = "Федор Достоевский"
books["Отцы и дети"] = "Иван Тургенев"

books_list = list(books.keys())
print(books_list)

unique_authors = set(books.values())
print(unique_authors)
