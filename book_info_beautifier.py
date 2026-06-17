book_info = "harper lee ; to kill a mocking bird ;1960 ; ISN 978-0-06-112008-4 ; 324 ;2999.4789"
book_info_data = book_info.split(' ; ')

book_author, book_title, publication_year, isbn, pages, price = book_info_data

print("The book " + book_title + "was written by " + book_author + "and published in " + publication_year + ". It has " + pages + "pages and " + isbn + "and costs " + price + '.')
