# Python_Test
Test work for  Effective Mobile
Задание: Разработка системы управления библиотекой

Структура програмы
1. Класс Book  - сущность описывающая книгу, модержит следующие поля:
               id - уникальный идентификатор, генерируется автоматически
               title - название книги
               author - автор книги
               year - год издания
               status - статус книги: “In Stock”, “Issued”
2. Класс Library - класс описывающий библиотечную систему, содержит следующие функции
               add_book - добавленик книги. При добавление необходимо указать: title,
                          author, year, после чего книга
                          добавляется в библитеку. id - генерируется автоматчиски, 
                          status - устанавливается "в наличии"
               delete_book - пользователь вводит id книги, которую нужно удалить
               search_book - пользователь может искать книги по title, author или year
               show_library - отображает все книги с их id, title, author, year, status
               change_status - пользователь вводит id книги и новый статус
               library - список обьектов Book содержит в себе колелкцию библиотеки
               load_book_list - загружает библиотеку из файла
               book_list - сохраняет библиотеу в файл
3. Файл main.py - точка входа в программу, в котором и будет крутиться программа в цикле.

4. Файл Dialog_messages  -  хранит в себе текстовые константы, на случай если где-то 
                           чтото нужно будет поменять, так будет удобнее. 
                            Чем каждый раз лазить по коду

