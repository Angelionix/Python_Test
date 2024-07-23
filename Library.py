import Book as b
import Dialog_messages as dm

class Library:
    free_ids = [] # список свободных айдишников, после удаления книг
    book_list = [] # Список книг

    # При инициализациии обьекта мы просто загружаем список книг из файла-хранилища
    def __init__(self):
        self.load_book_list()

    def add_book(self, title, author, year):
        '''
        Метод  add_book отвечает за добавление книги в хранилище.
        :param title: название книги
        :param author: имя автора
        :param year: год издания
        :return: возвращется список из значения Нон и сообщения об результате операции
        '''
        # Так как может возникнуть ситуация когда мы удалили книгу и у нас появился свобоный ИД, то сделали список с
        # этими ИД. И в начале мы проверяем есть ли в этом списке свободные ид, далее чекаем есть ли вообще в нашем
        # хранилище книги, и в зависимости от полученных результатов присваиваем айдишник
        if len(self.free_ids) == 0:
            if len(self.book_list) > 0:
                new_id = self.book_list[-1].id + 1
            else:
                new_id = 1
        else:
            new_id = self.free_ids.pop()
        # Добавляем в список книг новую
        new_book = b.Book(new_id, title, author, year, "In Stock")
        self.book_list.append(new_book)
        respond = [None, dm.OPERATION_SUCCESS]
        return  respond

    def delete_book(self, id):
        '''
        Метод удаления книги по ее идентификатору
        :param id: идентификатор книги
        :return: возвращется список из значения Нон и сообщения об результате операции
        '''
        respond = [None]
        # Чекаем есть ли вообще нужный ИД в базе
        if -1 < id and id <= len(self.book_list):
            for book in self.book_list:
                if id == book.id:
                    self.book_list.remove(book)
                    self.free_ids.append(id)
                    respond.append(dm.OPERATION_SUCCESS)
                    break
        else:
            respond.append(dm.WRONG_ID)
        return respond

    def search_book(self, request):
        '''
        Метод поиска книги по ее названию, имени автора или году
        :param request: строка запроса
        :return: возвращется список из книг и сообщения об результате операции
        '''
        responce = []
        books =[]
        for book in self.book_list:
            if request == book.title or request == book.author or request == book.year:
                books.append(book)
        if len(books) == 0:
            responce.append(None)
            responce.append(dm.OPERATION_FAILED)
        else:
            responce.append(books)
            responce.append(dm.OPERATION_SUCCESS)
        return responce

    def show_library(self):
        '''
         Метод для получения всего списка книг
         :return: возвращется список всех книг и сообщения об результате операции
         '''
        responce = []
        if len(self.book_list) > 0:
            responce.append(self.book_list)
            responce.append(dm.OPERATION_SUCCESS)
        else:
            responce.append(None)
            responce.append(dm.OPERATION_FAILED)
        return responce

    def change_status(self, id, new_status):
        '''
         Метод изменения статуса книги
         :param id: ИД книги
         :param new_status: Новый статус книги (In Stock или Issued)
         :return: возвращется список из книг значения Нон и сообщения об результате операции
         '''
        responce = []
        responce.append(None)
        if not (new_status == "In Stock" or new_status == "Issued"):
            responce.append(dm.WRONG_STATUS)
        else:
            if -1 < id and id <= len(self.book_list):
                for book in self.book_list:
                    if id == book.id:
                        book.status = new_status
                        responce.append(dm.OPERATION_SUCCESS)
                        break
            else:
                responce.append(dm.WRONG_ID)
        return responce

    def load_book_list(self):
        '''
         Метод загрузки списка книг из текстового хранилища
        '''
        try:
            with open('book_list.txt', 'r') as file:
                for line in file:
                    temp = line.split(sep='/')
                    new_book = b.Book(int(temp[0]), temp[1], temp[2], temp[3], temp[4][:-1])
                    self.book_list.append(new_book)
        except FileNotFoundError:
            print(dm.FILE_NOT_FOUND)

    def save_book_list(self):
        '''
         Метод сохранения списка книг в текстовое хранилище
        '''
        try:
            with open('book_list.txt', 'w') as file:
                for book in self.book_list:
                    book_line = f"{book.id}/{book.title}/{book.author}/{book.year}/{book.status}\n"
                    file.write(book_line)
        except FileNotFoundError:
            print(dm.FILE_NOT_FOUND)