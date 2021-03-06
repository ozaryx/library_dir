import library_dir as ld

library = 'library'

# Получить описание библиотеки
content = ld.read_library_description(library)
for line in content:
    print(line)

# Получить список книг (файлов)
book_list = ld.get_book_files(library)
for line in book_list:
    print(line)

# Получить информацию о книге
book_file = 'O_narodnom_vospitanii.txt'
book_info = ld.read_book_info(library, book_file)
print(book_info, '\n')

# Получить список авторов
authors = ld.get_authors(library)
print(authors, '\n')

# Получить информацию о всех книгах
books_info = ld.get_all_books_info(library)
print(books_info, '\n')
