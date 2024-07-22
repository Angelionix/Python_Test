import Book as b
import Dialog_messages as dm

class Library:
    free_ids = []
    book_list = []

    def __init__(self):
        pass

    def add_book(self, title, author, year):
        new_id = -1
        if len(self.free_ids) == 0:
            new_id = self.book_list[-1].id + 1
        else:
            new_id = self.free_ids.pop()
        new_book = b.Book(new_id, title, author, year, "В наличии")
        self.book_list.append(new_book)
        respond = [None, dm.OPERATION_SUCCESS]
        return  respond

    def delete_book(self, id):
        respond = [None]
        if -1 < id and id < len(self.book_list):
            for book in self.book_list:
                if id == book.id:
                    self.book_list.remove(book)
                    respond.append(dm.OPERATION_SUCCESS)
                    break
        else:
            respond.append(dm.WRONG_ID)
        return respond

    def search_book(self, request):
        responce = []
        for book in self.book_list:
            if request == book.title or request == book.author or request == book.year:
                responce.append(book)
        if len(responce) == 0:
            responce.append(None)
            responce.append(dm.OPERATION_FAILED)
        else:
            responce.append(dm.OPERATION_SUCCESS)
        return responce

    def show_library(self):
        responce = []
        if len(self.book_list) >0:
            responce.append(self.book_list)
            responce.append(dm.OPERATION_SUCCESS)
        else:
            responce.append(None)
            responce.append(dm.OPERATION_FAILED)
        return responce

    def change_status(self, id, new_status):
        responce = [None]
        if not (new_status == "В наличии" or new_status == "Выдана"):
            responce.append(dm.WRONG_STATUS)
        else:
            if -1 < id and id < len(self.book_list):
                for book in self.book_list:
                    if id == book.id:
                        book.status = new_status
                        responce.append(dm.OPERATION_SUCCESS)
                        break
            else:
                responce.append(dm.WRONG_ID)
        return responce

    def load_book_list(self):
        pass

    def save_book_list(self):
        pass