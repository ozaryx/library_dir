import library_dir as ld

library = 'library'

content = ld.read_library_description(library)
print(content, '\n')

book_list = ld.get_book_files(library)
print(book_list, '\n')

book_file = 'O_narodnom_vospitanii.txt'
book_info = ld.read_book_info(library, book_file)
print(book_info, '\n')

authors = ld.get_authors(library)
print(authors, '\n')

books_info = ld.get_all_books_info(library)
print(books_info, '\n')
