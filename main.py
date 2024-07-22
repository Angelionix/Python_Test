import Library as lib
import Dialog_messages as dm


def show_respond(respond):
    print(f"ID, Author,  title, year, status")
    for book in respond:
        print(f"{book.id} | {book.author} | {book.title} | {book.year} | {book.status}")


is_working = True
uncorrect_choose = True
choose = 0
library = lib.Library()

if __name__ == '__main__':
    print(dm.WELCOME_MESSAGE)
    while is_working:
        print(dm.SHOW_ALL_COMMAND)
        print(dm.ADD_BOOK_COMMAND)
        print(dm.DELETE_BOOK_COMMAND)
        print(dm.SEARCH_BOOK_COMMAND)
        print(dm.CHANGE_BOOK_STATUS_COMAND)
        print()
        print(dm.CHOOSE_OPTION_MESSAGE)
        while uncorrect_choose:
            try:
                temp = int(input())
                if temp > 0 and temp < 6:
                    choose = temp
                    uncorrect_choose = False
                else:
                    print(dm.WRONG_CHOOSE_NUMBER_MESSAGE)
            except:
                print(dm.WRONG_CHOOSE_INPUT_MESSAGE)
        match choose:
            case 1:
                library.show_library()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
        s = input()
        if s == " ":
          is_working = False