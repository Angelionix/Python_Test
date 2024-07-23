import Library as lib
import Dialog_messages as dm


def show_respond(respond):
    '''''
    Метод отображает ответы полученные при выполнении тех или иных операций.
    :param respond: список в котором в 0 индексе содержится полученные данные,
     а в 1-м сообщение о статусе операции
    '''''
    if None == respond[0]:
        print(respond[1])
    else:
        print(f"{'ID':4}| {'Author':30}| {'Title':50}| {'Year':4}| {'Status':8}")
        for book in respond[0]:
            print(f"{book.id:4}| {book.author:30}| {book.title:50}| {book.year:4}| {book.status:8}")

library = lib.Library()   # создаем онашу библиотеку, с ней мы и будем взаимодействовать
is_working = True         # данная переменная нам нужна чтобы знать когда завершить работу


'''''
В методе мейн мы закольцовываем весь код, чтобы программа могла выполняться столько скольно нам нужно, 
и когда мы хотим завершить работу мы изменяем переменную is_working
'''''
if __name__ == '__main__':
    print(dm.WELCOME_MESSAGE) # Приветственное сообщение
    while is_working:
        uncorrect_choose = True
        choose = 0
        #------ Блок вывод меню ---------
        print()
        print(dm.CHOOSE_OPTION_MESSAGE)
        print(dm.SHOW_ALL_COMMAND)
        print(dm.ADD_BOOK_COMMAND)
        print(dm.DELETE_BOOK_COMMAND)
        print(dm.SEARCH_BOOK_COMMAND)
        print(dm.CHANGE_BOOK_STATUS_COMAND)
        print(dm.EXIT_PROGRAMM)
        #------Выбираем пункт меню и проверяем что ввод корректный
        while uncorrect_choose:
            try:
                temp = int(input())
                if 0 < temp <= 6:
                    choose = temp
                    uncorrect_choose = False
                else:
                    print(dm.WRONG_CHOOSE_NUMBER_MESSAGE)
            except:
                print(dm.WRONG_CHOOSE_INPUT_MESSAGE)
        #--------------------------------------
        match choose:
            case 1:  # Показать список всех книг
                show_respond(library.show_library())
            case 2:  # добавить книгу
                new_title = input(dm.INPUT_TITLE_MESSAGE)
                new_author = input(dm.INPUT_AUTHOR_MESSAGE)
                new_year = ""
                uncorrect_year = True
                while uncorrect_year:
                    try:
                        temp = int(input(dm.INPUT_YEAR_MESSAGE))
                        if 1000 <= temp <= 9999:
                            new_year = str(temp)
                            uncorrect_year = False
                    except:
                        print(dm.UNCORRECT_YEAR)
                show_respond(library.add_book(new_title, new_author, new_year))
            case 3:  # удалить книгу
                uncorrect_id = True
                while uncorrect_id:
                    try:
                        selected_id = int(input(dm.INPUT_ID_MESSAGE))
                        uncorrect_id = False
                    except:
                        print(dm.WRONG_CHOOSE_INPUT_MESSAGE)
                show_respond(library.delete_book(selected_id))
            case 4:  # Найти книгу
                request = input(dm.INPUT_SEARCH_MESSAGE)
                show_respond(library.search_book(request))
            case 5:  # Изменить статус книги
                uncorrect_id = True
                while uncorrect_id:
                    try:
                        selected_id = int(input(dm.INPUT_ID_MESSAGE))
                        uncorrect_id = False
                    except:
                        print(dm.WRONG_CHOOSE_INPUT_MESSAGE)
                new_status = input(dm.INPUT_STATUS_MESSAGE)
                show_respond(library.change_status(selected_id, new_status))
            case 6:  # Закончить работу
                library.save_book_list()
                print(dm.SAVE_LIBRARY_MESSAGE)
                is_working = False