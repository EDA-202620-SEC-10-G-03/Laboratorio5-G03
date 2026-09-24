"""
 * ISIS1225 - Estructuras de Datos y Algoritmos
 * Laboratorio 5
 """

import csv
import os
import time
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt

# Ruta absoluta basada en la ubicación exacta del archivo logic.py
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'Data', 'GoodReads')

sort_algorithm = None
data_structure = None


def new_logic(user_data_structure):
    global data_structure
    if user_data_structure == "1":
        data_structure = al
    else:
        data_structure = lt

    catalog = {"books": None,
               "authors": None,
               "tags": None,
               "book_tags": None}

    # Inicialización completa de las estructuras del catálogo
    catalog["books"] = data_structure.new_list()
    catalog["authors"] = data_structure.new_list()
    catalog["tags"] = data_structure.new_list()
    catalog["book_tags"] = data_structure.new_list()

    return catalog


def load_data(catalog):
    books, authors = load_books(catalog)
    tag_size = load_tags(catalog)
    book_tag_size = load_books_tags(catalog)
    return books, authors, tag_size, book_tag_size


def load_books(catalog):
    booksfile = os.path.join(data_dir, 'books.csv')
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)


def load_tags(catalog):
    tagsfile = os.path.join(data_dir, 'tags.csv')
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        add_tag(catalog, tag)
    return tag_size(catalog)


def load_books_tags(catalog):
    bookstagsfile = os.path.join(data_dir, 'books_tags.csv')
    if not os.path.exists(bookstagsfile):
        bookstagsfile = os.path.join(data_dir, 'book_tags.csv')

    input_file = csv.DictReader(open(bookstagsfile, encoding='utf-8'))
    for booktag in input_file:
        add_book_tag(catalog, booktag)
    return book_tag_size(catalog)


def new_author(name):
    author = {"name": "", "books": None,  "average_rating": 0}
    author["name"] = name
    author["books"] = data_structure.new_list()
    return author


def new_tag(name, id):
    tag = {"name": "", "tag_id": ""}
    tag["name"] = name
    tag["tag_id"] = id
    return tag


def new_book_tag(tag_id, book_id, count):
    book_tag = {'tag_id': tag_id, 'book_id': book_id, 'count': count}
    return book_tag


def select_sort_algorithm(algo_opt):
    global sort_algorithm
    sort_algorithm = None
    algo_msg = None

    if algo_opt == 1:
        sort_algorithm = 1
        algo_msg = "Seleccionó la configuración - Selection Sort"
    elif algo_opt == 2:
        sort_algorithm = 2 
        algo_msg = "Seleccionó la configuración - Insertion Sort"
    elif algo_opt == 3:
        sort_algorithm = 3
        algo_msg = "Seleccionó la configuración - Shell Sort"
    elif algo_opt == 4:
        sort_algorithm = 4 
        algo_msg = "Seleccionó la configuración - Merge Sort"
    elif algo_opt == 5:    
        sort_algorithm = 5 
        algo_msg = "Seleccionó la configuración - Quick Sort"
    else:
        algo_msg = "No seleccionó una configuración válida"
    
    return sort_algorithm, algo_msg


def set_book_sublist(catalog, size):
    books = catalog["books"]
    catalog["book_sublist"] = data_structure.sub_list(books, 0, size)
    return catalog


def get_books_by_author(catalog, author_name):
    pos_author = data_structure.is_present(
        catalog['authors'], author_name, compare_authors)
    if pos_author >= 0:
        author = data_structure.get_element(catalog['authors'], pos_author)
        return author
    return None


def get_book_info_by_book_id(catalog, book_id):
    pos_book = data_structure.is_present(
        catalog['books'], book_id, compare_book_ids)
    if pos_book >= 0:
        book = data_structure.get_element(catalog['books'], pos_book)
        return book
    return None


def count_books_by_tag(catalog, tag_name):
    pos_tag = data_structure.is_present(
        catalog['tags'], tag_name, compare_tag_names)

    if pos_tag >= 0:
        tag = data_structure.get_element(catalog['tags'], pos_tag)
        tag_id = tag['tag_id']
        total_processed = 0

        for i in range(data_structure.size(catalog['book_tags'])):
            book_tag = data_structure.get_element(catalog['book_tags'], i)
            if book_tag is not None and book_tag['tag_id'] == tag_id:
                total_processed += 1

        return total_processed
    return 0


def book_size(catalog):
    return data_structure.size(catalog["books"])


def author_size(catalog):
    return data_structure.size(catalog["authors"])


def tag_size(catalog):
    return data_structure.size(catalog["tags"])


def book_tag_size(catalog):
    return data_structure.size(catalog["book_tags"])


def compare_authors(author_or_name1, author_or_name2):
    if isinstance(author_or_name1, str):
        name = author_or_name1
        author = author_or_name2
    elif isinstance(author_or_name2, str):
        name = author_or_name2
        author = author_or_name1
    else:
        name = author_or_name1['name']
        author = author_or_name2

    author_name = author['name']
    
    if name.lower() == author_name.lower():
        return 0
    elif name.lower() > author_name.lower():
        return 1
    return -1


def compare_tag_names(tag_or_name1, tag_or_name2):
    if isinstance(tag_or_name1, str):
        name = tag_or_name1
        tag = tag_or_name2
    elif isinstance(tag_or_name2, str):
        name = tag_or_name2
        tag = tag_or_name1
    else:
        name = tag_or_name1['name']
        tag = tag_or_name2

    if name == tag['name']:
        return 0
    elif name > tag['name']:
        return 1
    return -1


def compare_book_ids(id_or_book1, id_or_book2):
    if isinstance(id_or_book1, (int, str)):
        book_id = int(id_or_book1)
        book = id_or_book2
    elif isinstance(id_or_book2, (int, str)):
        book_id = int(id_or_book2)
        book = id_or_book1
    else:
        book_id = int(id_or_book1["goodreads_book_id"])
        book = id_or_book2

    target_id = int(book["goodreads_book_id"])

    if book_id == target_id:
        return 0
    elif book_id > target_id:
        return 1
    return -1


def eval_ratings(book1, book2):
    return float(book1['average_rating']) > float(book2['average_rating'])


def sort_books(catalog):
    sorted_books = catalog["book_sublist"]
    start_time = get_time()

    if sort_algorithm == 1:
        sorted_books_s = data_structure.selection_sort(sorted_books, eval_ratings)
    elif sort_algorithm == 2:
        sorted_books_s = data_structure.insertion_sort(sorted_books, eval_ratings)
    elif sort_algorithm == 3:
        sorted_books_s = data_structure.shell_sort(sorted_books, eval_ratings)
    elif sort_algorithm == 4:
        sorted_books_s = data_structure.merge_sort(sorted_books, eval_ratings)
    elif sort_algorithm == 5:
        sorted_books_s = data_structure.quick_sort(sorted_books, eval_ratings)
    else:
        sorted_books_s = sorted_books

    end_time = get_time()
    delta = delta_time(start_time, end_time)

    return sorted_books_s, delta


def add_book(catalog, book):
    book["goodreads_book_id"] = int(book["goodreads_book_id"])
    data_structure.add_last(catalog['books'], book)
    authors = book['authors'].split(",")
    for author in authors:
        add_book_author(catalog, author.strip(), book)
    return catalog


def add_book_author(catalog, author_name, book):
    authors = catalog['authors']
    pos_author = data_structure.is_present(
        authors, author_name, compare_authors)
    if pos_author >= 0:
        author = data_structure.get_element(authors, pos_author)
    else:
        author = new_author(author_name)
        data_structure.add_last(authors, author)
    data_structure.add_last(author['books'], book)
    return catalog


def add_tag(catalog, tag):
    t = new_tag(tag['tag_name'], tag['tag_id'])
    data_structure.add_last(catalog['tags'], t)
    return catalog


def add_book_tag(catalog, book_tag):
    t = new_book_tag(book_tag['tag_id'],
                     book_tag['goodreads_book_id'], book_tag['count'])
    data_structure.add_last(catalog['book_tags'], t)
    return catalog


def get_time():
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    return float(end - start)