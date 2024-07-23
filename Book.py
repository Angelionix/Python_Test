class Book:
    id = 0
    title = ""
    author = ""
    year = ""
    status = ""

    def __init__(self, id, title, author, year, status):
        '''
        Класс Book - сущность описывающая книгу\n
        Имеет следующие поля: \n
        id -- идентификатор книги \n
        title -- название книги\n
        author -- имя автора\n
        year -- год издания\n
        status -- статус книги (In Stock или Issue)
        '''
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status