class Book:
    id = 0
    title = ""
    author = ""
    year = ""
    status = ""

    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status