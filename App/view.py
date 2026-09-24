"""
 * ISIS1225 - Estructuras de Datos y Algoritmos
 * Laboratorio 5
 """

import sys
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt

# Ajuste del límite de recursión de Python recomendado por el enunciado
sys.setrecursionlimit(10000)

data_structure = None


def new_logic(data_structure):
    control = logic.new_logic(data_structure)
    return control


def print_menu():
    print("\n--- Menú Principal ---")
    print("0- Seleccionar estructura de datos")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la información de un libro")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Seleccionar el algoritmo de ordenamiento")
    print("6- Seleccionar muestra de libros")
    print("7- Ordenar los libros por rating")
    print("8- Salir")


def select_data_structure():
    print("\nEscoge la estructura de datos a usar:")
    print("1 - Array_list")
    print("2 - Single_linked_list")
    
    sub_input = ""
    while sub_input == "":
        sub_input = input("\nSeleccione una opción: ")
        global data_structure
        if sub_input == "1":
            data_structure = al
            print("Has elegido Array_list")
            return sub_input
        elif sub_input == "2":
            data_structure = lt
            print("Has elegido Single_linked_list")
            return sub_input
        else:
            print("Opción no válida en el submenú")
            sub_input = ""


def load_data(control):
    books, authors, tags, book_tags = logic.load_data(control)
    return books, authors, tags, book_tags


def print_author_data(author):
    if author:
        print("Autor encontrado: " + author["name"])
        print("Promedio: " + str(author["average_rating"]))
        print("Total de libros: " + str(data_structure.size(author["books"])))
        for book_pos in range(0, data_structure.size(author['books'])):
            book = data_structure.get_element(author['books'], book_pos)
            print("Titulo: " + book["title"] + "  ISBN: " + book["isbn"])
    else:
        print("No se encontró el autor")
        

def print_book_info(book):
    if book:
        print('Titulo: ' + book['title'] + ' | ISBN: ' +
              book['isbn'] + ' | Rating: ' + str(book['average_rating']) +
              ' | Work text reviews count: ' + str(book['work_text_reviews_count']))
    else:
        print('No se encontraron libros')


def print_sort_results(sort_books_tuple, sample=3):
    """
    Imprime la información de los primeros 'sample' libros ordenados.
    """
    sorted_books = sort_books_tuple[0]
    total = data_structure.size(sorted_books)
    limit = min(sample, total)
    
    print(f"\nMostrando los primeros {limit} libros mejor calificados:")
    for book_pos in range(0, limit):
        book = data_structure.get_element(sorted_books, book_pos)
        print_book_info(book)


algo_str = """
Seleccione el algoritmo de ordenamiento:
1. Selection Sort
2. Insertion Sort
3. Shell Sort
4. Merge Sort
5. Quick Sort
"""
                 
exit_opt_lt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


def main():
    working = True
    control = None
    size = 0

    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        
        if not inputs:
            continue

        option = int(inputs[0])
        
        if option == 0:
            user_data_structure = select_data_structure()
            control = new_logic(user_data_structure)
            
        elif option == 1:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = load_data(control)
            print(f"Carga completa:")
            print(f"- Libros cargados: {bk}")
            print(f"- Autores cargados: {at}")
            print(f"- Etiquetas (tags) cargadas: {tg}")
            print(f"- Asociaciones libro-tag cargadas: {bktg}")

        elif option == 2:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            number = input("Ingrese el id del libro que desea buscar: ")
            book = logic.get_book_info_by_book_id(control, int(number))
            print_book_info(book)

        elif option == 3:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            authorname = input("Nombre del autor a buscar: ")
            author = logic.get_books_by_author(control, authorname)
            print_author_data(author)

        elif option == 4:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            label = input("Etiqueta a buscar: ")
            book_count = logic.count_books_by_tag(control, label)
            print('Se encontraron: ', book_count, ' Libros')
                 
        elif option == 5:
            algo_opt = input(algo_str)
            algo_opt = int(algo_opt)
            algo_msg = logic.select_sort_algorithm(algo_opt)
            print(algo_msg[1])
            
        elif option == 6:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            logic.set_book_sublist(control, size)
            print(f"Sublista configurada con {size} libros.")

        elif option == 7:
            if control is None:
                print("Primero debe seleccionar la estructura de datos (Opción 0).")
                continue
            print("Ordenando los libros por rating ...")
            result = logic.sort_books(control)
            print_sort_results(result, sample=3)
            print("Tiempo de ejecución:", f"{result[1]:.3f}", "[ms]")

        elif option == 8:
            end_str = "¿Desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            if opt_usr in exit_opt_lt:
                working = False
                print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)


if __name__ == "__main__":
    main()