# TODO Найдите количество книг, которое можно разместить на дискете
total_size = 1.44
number_of_pages = 100
string_in_page = 50
symbols_in_string = 25
weight_of_one_symbol = 4

total_symbols_in_book = number_of_pages * string_in_page * symbols_in_string
total_size_of_one_book = total_symbols_in_book * weight_of_one_symbol
weight_in_Kb = total_size_of_one_book/1024
weight_in_Mb = weight_in_Kb/1024

books = total_size/weight_in_Mb
result = round(books)
print("Количество книг, помещающихся на дискету:", result)
