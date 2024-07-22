import Library as lib
import Dialog_messages as dm


def show_respond(respond):
    if None == respond[0]:
        print(respond[1])
    else:
        print(f"{'ID':4}| {'Author':30}| {'Title':50}| {'Year':4}| {'Status':8}")
        for book in respond[0]:
            print(f"{book.id:4}| {book.author:30}| {book.title:50}| {book.year:4}| {book.status:8}")

library = lib.Library()
is_working = True



if __name__ == '__main__':
    print(dm.WELCOME_MESSAGE)
    while is_working:
        uncorrect_choose = True
        choose = 0

        print()
        print(dm.CHOOSE_OPTION_MESSAGE)
        print(dm.SHOW_ALL_COMMAND)
        print(dm.ADD_BOOK_COMMAND)
        print(dm.DELETE_BOOK_COMMAND)
        print(dm.SEARCH_BOOK_COMMAND)
        print(dm.CHANGE_BOOK_STATUS_COMAND)
        print(dm.EXIT_PROGRAMM)

        while uncorrect_choose:
            try:
                temp = int(input())
                if temp > 0 and temp <= 6 :
                    choose = temp
                    uncorrect_choose = False
                else:
                    print(dm.WRONG_CHOOSE_NUMBER_MESSAGE)
            except:
                print(dm.WRONG_CHOOSE_INPUT_MESSAGE)

        match choose:
            case 1:
                show_respond(library.show_library())
            case 2:
                new_title = input("Введите название книги: ")
                new_author = input("Введите имя автора: ")
                new_year = input("Введите год издания: ")
                show_respond(library.add_book(new_title, new_author, new_year))
            case 3:
                id_to_del = int(input("Введите id книги которую выхотите удалить из базы: "))
                show_respond(library.delete_book(id_to_del))
            case 4:

                pass
            case 5:
                pass
            case 6:
                is_working = False